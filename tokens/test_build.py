"""Tests for the token build. Run: python3 -m unittest discover tokens"""
import unittest
from pathlib import Path

import build

ROOT = Path(__file__).resolve().parent.parent


class ColourMaths(unittest.TestCase):
    def test_rgb565_packs_5_6_5_bits(self):
        self.assertEqual(build.rgb565("#ffffff"), 0xFFFF)
        self.assertEqual(build.rgb565("#000000"), 0x0000)
        self.assertEqual(build.rgb565("#ff0000"), 0xF800)
        self.assertEqual(build.rgb565("#00ff00"), 0x07E0)
        self.assertEqual(build.rgb565("#0000ff"), 0x001F)

    def test_contrast_matches_wcag(self):
        self.assertEqual(build.contrast("#000000", "#ffffff"), 21.0)
        self.assertEqual(build.contrast("#ffffff", "#ffffff"), 1.0)
        self.assertEqual(build.contrast("#ff3030", "#07080c"), build.contrast("#07080c", "#ff3030"))


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = build.load()

    def test_logo_colours_match_the_logo_file(self):
        svg = (ROOT / "logo" / "chilichip-logo.svg").read_text()
        for name, colour in self.tokens["color"].items():
            if colour["source"] == "logo":
                self.assertIn(f'fill="{colour["value"]}"', svg, name)

    def test_every_theme_role_names_a_real_colour(self):
        for theme, roles in self.tokens["theme"].items():
            for role, colour in roles.items():
                self.assertIn(colour, self.tokens["color"], f"{theme}.{role}")

    def test_no_role_is_named_like_a_colour(self):
        # Both become --cc-<name>, so a shared name would overwrite the colour.
        for theme, roles in self.tokens["theme"].items():
            self.assertFalse(set(roles) & set(self.tokens["color"]), theme)

    def test_text_roles_are_readable(self):
        # WCAG AA for normal text is 4.5:1.
        for theme, roles in self.tokens["theme"].items():
            hexes = {role: self.tokens["color"][c]["value"] for role, c in roles.items()}
            for role in ("text", "muted", "accent-text", "link", "success", "warning", "danger"):
                if role in hexes:
                    for bg in ("bg", "surface"):
                        self.assertGreaterEqual(build.contrast(hexes[role], hexes[bg]), 4.5, f"{theme}: {role} on {bg}")
            self.assertGreaterEqual(build.contrast(hexes["on-accent"], hexes["accent"]), 4.5, theme)


class Outputs(unittest.TestCase):
    def test_generated_files_are_up_to_date(self):
        for path, content in build.outputs(build.load()).items():
            self.assertTrue(path.exists(), f"{path} is missing. Run: python3 tokens/build.py")
            self.assertEqual(path.read_bytes(), content, f"{path} is stale. Run: python3 tokens/build.py")

    def test_css_has_both_themes(self):
        css = build.css(build.load())
        self.assertIn("--cc-chili: #ff3030;", css)
        self.assertIn("--cc-bg: var(--cc-ink-0);", css)
        self.assertIn('[data-theme="light"]', css)
        self.assertIn("--cc-bg: var(--cc-bone);", css)

    def test_header_has_console_colours(self):
        hpp = build.hpp(build.load())
        self.assertIn("inline constexpr Rgb chili{0xff, 0x30, 0x30};", hpp)
        self.assertIn("inline constexpr Rgb bg = color::black;", hpp)


if __name__ == "__main__":
    unittest.main()

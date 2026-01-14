"""Generate household PDF reports."""

import os
from pathlib import Path

from weasyprint import HTML, CSS

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "templates"
STYLES_DIR = PROJECT_ROOT / "styles"
OUTPUT_DIR = PROJECT_ROOT / "output"


def render_template(template_name: str, **kwargs) -> str:
    """Load an HTML template and substitute placeholders.

    Uses simple {{placeholder}} syntax for substitution.
    """
    template_path = TEMPLATES_DIR / template_name
    content = template_path.read_text()

    for key, value in kwargs.items():
        content = content.replace(f"{{{{{key}}}}}", str(value))

    return content


def generate_household_pages(households: list[dict], output_filename: str = "households.pdf"):
    """Generate a PDF with one page per household.

    Args:
        households: List of household dicts, each must have a 'name' key.
        output_filename: Name of the output PDF file.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Build combined HTML with all households
    pages_html = []
    for household in households:
        page = render_template("household-page.html", household_name=household["name"])
        # Extract just the body content for combining
        # Find the page div and use it
        start = page.find('<div class="page')
        end = page.rfind('</div>') + len('</div>')
        pages_html.append(page[start:end])

    # Combine into single document
    combined_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Household Report</title>
</head>
<body>
{"".join(pages_html)}
</body>
</html>
"""

    # Generate PDF
    base_css = CSS(filename=str(STYLES_DIR / "base.css"))
    output_path = OUTPUT_DIR / output_filename

    HTML(string=combined_html, base_url=str(PROJECT_ROOT)).write_pdf(
        output_path,
        stylesheets=[base_css]
    )

    print(f"Generated: {output_path}")
    return output_path

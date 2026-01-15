"""Generate household PDF reports."""

import re
from datetime import date
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


def sanitize_filename(name: str) -> str:
    """Convert a name to a safe filename."""
    # Replace special characters with underscores
    safe = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Replace multiple spaces/underscores with single underscore
    safe = re.sub(r'[\s_]+', '_', safe)
    # Remove leading/trailing underscores
    return safe.strip('_')


def reorder_name_last_first(name: str) -> str:
    """Reorder a name to put the last name first.

    Examples:
        "Aaron & Jenny Stull" -> "Stull Aaron & Jenny"
        "Adam D Egelberg" -> "Egelberg Adam D"
    """
    parts = name.split()
    if len(parts) <= 1:
        return name
    last_name = parts[-1]
    first_parts = ' '.join(parts[:-1])
    return f"{last_name} {first_parts}"


def format_currency(value: float) -> str:
    """Format a number as currency."""
    return f"${value:,.2f}"


def build_account_rows(accounts: list[dict]) -> str:
    """Build HTML table rows for accounts."""
    rows = []
    for account in accounts:
        row = f"""<tr>
                    <td>{account['name']}</td>
                    <td>{account['type']}</td>
                    <td class="text-right">{format_currency(account['balance'])}</td>
                </tr>"""
        rows.append(row)
    return "\n                ".join(rows)


def generate_household_report(
    household_name: str,
    accounts: list[dict],
    as_of_date: date | None = None,
    report_name: str = "Quarterly Report"
) -> Path:
    """Generate a PDF report for a single household.

    Args:
        household_name: Name of the household.
        accounts: List of account dicts with keys: name, type, balance.
        as_of_date: Date for the report. Defaults to today.
        report_name: Name of the report type for the filename.

    Returns:
        Path to the generated PDF file.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    if as_of_date is None:
        as_of_date = date.today()

    # Build filename: "Last First - Quarterly Report - 2026-01-14.pdf"
    date_str = as_of_date.strftime("%Y-%m-%d")
    reordered_name = reorder_name_last_first(household_name)
    safe_name = sanitize_filename(reordered_name)
    filename = f"{safe_name} - {report_name} - {date_str}.pdf"

    # Build account table data
    account_rows = build_account_rows(accounts)
    total_balance = format_currency(sum(a["balance"] for a in accounts))

    # Render HTML
    html_content = render_template(
        "household-page.html",
        household_name=household_name,
        account_rows=account_rows,
        total_balance=total_balance
    )

    # Generate PDF
    base_css = CSS(filename=str(STYLES_DIR / "base.css"))
    output_path = OUTPUT_DIR / filename

    HTML(string=html_content, base_url=str(PROJECT_ROOT)).write_pdf(
        output_path,
        stylesheets=[base_css]
    )

    return output_path

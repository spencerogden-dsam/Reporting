# CLAUDE.md - AI Assistant Guidelines for Reporting

This file provides guidance for AI assistants (like Claude) working on this codebase.

## Repository Overview

**Repository**: Reporting
**Language**: Python
**Purpose**: Generate PDF reports for clients using data from WealthBox and Orion

## Data Pipeline

```
WealthBox API ──┐
                ├──► Data Processing ──► Calculations ──► Charts ──► HTML ──► PDF
Orion API ──────┘
```

1. **Data Gathering**: Fetch raw data using `orionapi` and `wealthbox` Python modules
2. **Processing**: Perform calculations on the data
3. **Visualization**: Create charts as needed
4. **Rendering**: Generate HTML from templates
5. **Output**: Convert HTML to PDF for client delivery

## Project Structure

```
Reporting/
├── CLAUDE.md                  # AI assistant guidelines (this file)
├── generate_households.py     # Main script: generate household PDF report
├── requirements.txt           # Python dependencies
├── templates/                 # HTML templates (standalone files)
│   └── household-page.html    # Single household page template
├── styles/                    # CSS stylesheets (standalone files)
│   └── base.css               # Shared styles across all reports
├── reports/                   # Report generation modules
│   └── household_report.py    # Household PDF generator
├── data/                      # Data fetching and processing
│   └── orion.py               # Orion API utilities
├── charts/                    # Chart generation
│   └── *.py
└── output/                    # Generated PDFs (gitignored)
```

## Design Principles

### HTML/CSS Guidelines

- **Keep it simple**: Use vanilla HTML and CSS - no frameworks unless truly necessary
- **Standalone files**: Templates and stylesheets should be simple, self-contained files
- **Consistent styling**: All reports share common styles from `base.css`
- **Print-first**: Design for PDF/print output, not screen viewing

### Print/PDF Considerations

- Use CSS `@page` rules for page size, margins, headers, footers
- Use `page-break-before`, `page-break-after`, `page-break-inside` for layout control
- Avoid elements that don't translate well to print (animations, hover states)
- Test with actual PDF output, not just browser print preview
- Consider using `@media print` for print-specific styles

### CSS Structure

```css
/* base.css - shared across all reports */
@page {
    size: letter;
    margin: 1in;
}

/* print.css - print-specific overrides */
@media print {
    /* print styles */
}
```

## Dependencies

- `orionapi` - Orion API access (PyPI)
- `wealthbox` - WealthBox API access (PyPI)
- `weasyprint` - HTML/CSS to PDF conversion

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Generate household report (requires ORION_USERNAME and ORION_PASSWORD env vars)
python generate_households.py

# Run tests
python -m pytest
```

## Coding Standards

### Python

- Follow PEP 8 style guidelines
- Use type hints where practical
- Keep functions focused and single-purpose

### File Naming

- Python: `snake_case.py`
- HTML templates: `report-name.html`
- CSS: `purpose.css`

## Future: Report Delivery

Report delivery will match generated PDFs with client emails and create draft emails for review.

### Workflow

1. **Match households**: Match Orion household names to WealthBox household names (name matching for now)
2. **Get recipients**: For each WealthBox household, get primary email for adult members only:
   - Include: Head, Spouse, Partner
   - Exclude: Child and other relationship types
3. **Upload to Box**: Create one folder per household per delivery, upload report PDF(s), generate shared link with expiration date
4. **Create Gmail drafts**: Use Google Workspace API to create draft emails in user's account using a template (stored in repo). Draft includes:
   - Recipients (to field)
   - Subject line
   - Body with secure Box link
5. **User review**: Drafts remain in user's Gmail draft folder for review/editing before manual send

### Configuration

- **Gmail account**: `mverhelst@gmail.net` (may become per-household setting later)
- **Box folder structure**: One folder per household per delivery
- **Email template**: Stored in this repository

### Dependencies (future)

- `wealthbox` - WealthBox API for household/contact lookup
- Google Workspace API - Gmail draft creation
- Box API - Folder creation, file upload, shared links

## AI Assistant Instructions

When working on this codebase:

1. **Read before modifying**: Always read existing code before making changes
2. **Minimal changes**: Make only the changes necessary to complete the task
3. **Preserve style**: Match existing code style and patterns
4. **Simple solutions**: Prefer vanilla HTML/CSS over frameworks
5. **Print-aware**: Always consider how changes affect PDF output
6. **Consistent styling**: New reports should use shared styles from `base.css`

### Areas Requiring Extra Care

- **API credentials**: Never commit WealthBox or Orion API keys
- **Page layout**: Test PDF output when modifying templates or styles
- **Cross-report consistency**: Changes to base styles affect all reports

### Common Patterns

- Templates use simple HTML with placeholder variables
- CSS is organized: base styles shared, report-specific styles separate
- Data flows: API → processing → charts → template → PDF

---

*Last updated: January 2026*

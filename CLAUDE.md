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
├── CLAUDE.md              # AI assistant guidelines (this file)
├── templates/             # HTML templates (standalone files)
│   └── *.html
├── styles/                # CSS stylesheets (standalone files)
│   ├── base.css           # Shared styles across all reports
│   └── print.css          # Print/PDF-specific styles
├── reports/               # Report generation modules
│   └── *.py
├── data/                  # Data fetching and processing
│   └── *.py
├── charts/                # Chart generation
│   └── *.py
└── output/                # Generated PDFs (gitignored)
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

- `orionapi` - Custom module for Orion API access
- `wealthbox` - Custom module for WealthBox API access
- PDF generation library (TBD - likely weasyprint, pdfkit, or similar)

## Commands

```bash
# (To be documented as project develops)
# python -m reports.quarterly    # Generate quarterly report
# python -m pytest               # Run tests
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

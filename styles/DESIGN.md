# Design Guidelines

This document defines the visual standards for Dock Street reports.

## Typography

- **Font**: Garamond (fallback: Times New Roman, serif)
- **Body text**: 11pt
- **Small text**: 9pt (footnotes, captions)
- **H1**: 24pt (household name, report title)
- **H2**: 16pt (section headers)
- **H3**: 12pt (subsection headers)

## Page Layout

- **Page size**: Letter (8.5" x 11")
- **Margins**: 0.75" all sides
- **Default style**: Black text on white background

## Color Philosophy

Reports are **black and white by default**. Color is reserved for charts and intentional emphasis.

> "If your chart looks colorful, you're doing it wrong."

---

## Dock Street Color Palette

### Primary / Core (Blue Owns the Data)

Use for 80-90% of chart elements. Communicates seriousness, trust, continuity.

| Name       | Hex       | Usage                                      |
|------------|-----------|---------------------------------------------|
| Corporate  | `#061441` | Primary series, key totals, anchor color    |
| Water      | `#244076` | Benchmark, secondary important data         |
| Sky        | `#506CAC` | Tertiary comparison                         |
| Cloud      | `#899DC2` | Historical, projected, de-emphasized        |

### Secondary / Natural (Conditional, Not Decorative)

| Name       | Hex       | Usage                                      |
|------------|-----------|---------------------------------------------|
| Flower     | `#43486C` | Utility: axis labels, annotations, gridlines |
| Grass      | `#254E45` | Positive cash flow, operational strength    |
| Foliage    | `#76997D` | Sustainable growth, organic concepts        |

**Do not** use green just because "up is good." Use only when the concept is organic or operational.

### Neutrals / Accents (Flags, Not Series)

| Name       | Hex       | Usage                                      |
|------------|-----------|---------------------------------------------|
| Clean      | `#EDE6D5` | Backgrounds, chart areas, table fills only  |
| Sun        | `#CC7F30` | Highlight, callout, threshold (sparingly)   |
| Build      | `#812A15` | Alert, emphasis (sparingly)                 |

**Rule**: If orange or red shows up more than once in a chart, it's too much.

---

## Chart Color Stack (Default Order)

When building charts, use colors in this order:

1. **Primary line/bar**: Corporate (`#061441`)
2. **Benchmark**: Water (`#244076`)
3. **Secondary comparison**: Sky (`#506CAC`)
4. **Historical/projection**: Cloud (`#899DC2`)
5. **Highlight/alert**: Sun or Build (rare)
6. **Background**: Clean (`#EDE6D5`)
7. **Labels/axes**: Flower (`#43486C`)

**Max 4 colors per chart** unless there's a compelling reason.

---

## Color Usage Rules

### Corporate is the Anchor
- Use for primary series, key totals, "our strategy" line
- Never use for background fills or minor data—it's too heavy

### Water & Sky for Comparisons
- Water = secondary but important (benchmark, peer group)
- Sky = tertiary comparison
- Cloud = historical, projected, or de-emphasized
- Think **hierarchy**, not decoration

### Green is Conditional
Use Grass/Foliage only for:
- Positive cash flow
- Operating strength
- Sustainable growth metrics

### Warm Colors are Flags
Sun and Build are accent-only:
- Highlights
- Callouts
- Threshold breaches
- One-off emphasis

**Never** use for full data series.

### Clean is for Space
- Backgrounds, chart areas, table fills
- Never for lines, bars, or labels—it will wash out

### Flower is Infrastructure
- Axis labels, secondary annotations, gridlines
- Invisible when done right

---

## Spacing Scale

Consistent spacing throughout reports:

| Token       | Value | Usage                          |
|-------------|-------|--------------------------------|
| `--space-xs`| 4pt   | Tight spacing, inline elements |
| `--space-sm`| 8pt   | Related items, table padding   |
| `--space-md`| 16pt  | Paragraphs, standard gaps      |
| `--space-lg`| 24pt  | Section breaks                 |
| `--space-xl`| 32pt  | Major divisions                |

---

## Implementation

All values are defined in `tokens.css` as CSS custom properties. To adjust any value:

1. Edit `styles/tokens.css`
2. Regenerate PDFs to see changes

Example token references:
```css
color: var(--color-corporate);
font-size: var(--font-size-h2);
margin-bottom: var(--space-lg);
```

---

*Last updated: January 2026*

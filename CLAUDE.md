# CLAUDE.md - AI Assistant Guidelines for Reporting

This file provides guidance for AI assistants (like Claude) working on this codebase.

## Repository Overview

**Repository**: Reporting
**Status**: New/Initial setup
**Purpose**: Reporting system (to be defined as development progresses)

## Project Structure

```
Reporting/
├── CLAUDE.md          # AI assistant guidelines (this file)
└── (empty - awaiting initial development)
```

As the project grows, update this section with the actual structure.

## Development Workflow

### Branch Strategy

- Main branch: `main` (or as configured)
- Feature branches: Use descriptive names prefixed appropriately (e.g., `feature/`, `fix/`, `claude/`)
- Always create pull requests for code review before merging

### Commit Conventions

- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update", "Remove")
- Keep the first line under 72 characters
- Reference issue numbers when applicable

Example:
```
Add user authentication module

- Implement JWT-based authentication
- Add login/logout endpoints
- Include unit tests for auth flow

Fixes #123
```

## Coding Standards

### General Guidelines

1. **Code Quality**: Write clean, readable, and maintainable code
2. **Documentation**: Add comments for complex logic; keep code self-documenting where possible
3. **Testing**: Include tests for new functionality
4. **Security**: Never commit secrets, API keys, or credentials

### File Naming

- Use lowercase with hyphens for file names (e.g., `user-report.py`)
- Use descriptive names that indicate the file's purpose

## Commands

Document key commands here as they are established:

```bash
# Example commands (update as project develops)
# npm install        # Install dependencies
# npm test           # Run tests
# npm run build      # Build project
# npm run lint       # Run linter
```

## Architecture Notes

Document key architectural decisions and patterns here as the project develops:

- (To be documented)

## AI Assistant Instructions

When working on this codebase:

1. **Read before modifying**: Always read existing code before making changes
2. **Minimal changes**: Make only the changes necessary to complete the task
3. **Preserve style**: Match existing code style and patterns
4. **Test changes**: Run tests after making modifications
5. **Update documentation**: Keep this CLAUDE.md file current as the project evolves

### Areas Requiring Extra Care

- (To be documented as sensitive areas are identified)

### Common Pitfalls

- (To be documented as issues are discovered)

## Dependencies

Document major dependencies and their purposes here:

- (None yet)

## Environment Setup

Document environment setup requirements here:

```bash
# Environment setup steps (to be documented)
```

## Testing

Document testing approach and commands:

- (Testing strategy to be documented)

## Deployment

Document deployment process:

- (Deployment process to be documented)

---

*Last updated: January 2026*
*Update this file whenever significant changes are made to the codebase structure, workflows, or conventions.*

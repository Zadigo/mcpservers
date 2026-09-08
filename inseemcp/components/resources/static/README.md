# INSEE Enterprise Dataset

## Overview

This MCP server provides access to French enterprise and establishment data from the INSEE enterprise APIs.

The dataset can be used to:

- identify French legal units;
- retrieve establishments;
- search legal units by name;
- search establishments by name;
- retrieve information using SIREN or SIRET;
- investigate relationships between legal units and establishments;
- retrieve information about French associations where supported.

The data originates from INSEE. This MCP server does not independently verify or modify the information returned by INSEE.

---

## Core concepts

The dataset distinguishes between:

### Legal unit

A legal unit is identified by a SIREN.

A legal unit can have one or more establishments.

### Establishment

An establishment represents a specific location or operational unit belonging to a legal unit.

An establishment is identified by a SIRET.

### SIREN

A SIREN is a 9-digit identifier for a legal unit.

### SIRET

A SIRET is a 14-digit identifier for an establishment.

A SIRET contains the SIREN of its associated legal unit plus an
establishment-specific NIC.

---

## Identifier relationships

    SIREN
      │
      ▼
  Legal unit
      │
      ├── SIRET
      ├── SIRET
      └── SIRET

Never treat SIREN and SIRET as interchangeable.

If the user provides a SIREN and asks about the company/legal unit, use the legal-unit tools.

If the user provides a SIRET and asks about an establishment, use the establishment tools.

If the user provides a SIREN and asks for its establishments, retrieve the establishments associated with that legal unit.

---

## Search behavior

Name searches may return multiple results.

A prefix search is not an exact-name search.

For example:

"Michelin"

may match names beginning with "Michelin".

Do not assume that a name match represents a unique legal unit.

When multiple results exist, use available identifiers, location, activity, or legal information to distinguish them.

---

## Data interpretation rules

- SIREN → legal unit
- SIRET → establishment
- One legal unit may have multiple establishments.
- Multiple establishments can therefore share the same SIREN.
- A name is not necessarily a unique identifier.
- Search results should be treated as INSEE records, not as independently verified information.

---

## Handling missing results

If a lookup returns no result:

1. Do not invent a company or establishment.
2. Report that no matching INSEE record was found.
3. If appropriate, ask the user whether they want to search by another identifier or by name.

---

## Data freshness

The information returned by this server depends on the underlying INSEE API and its available historical/current data.

Do not describe a record as "current" unless the API response supports that conclusion.

If a date parameter is available, use it when the user explicitly asks about the state of an entity at a particular date.

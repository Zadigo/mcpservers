# Search behavior

## Exact identifier searches

Identifier searches should be used when the user provides a complete SIREN or SIRET.

## Prefix searches

Prefix searches return records whose search field begins with the provided value.

They should not be interpreted as exact matches.

## Name searches

Name searches operate on INSEE denomination fields.

A company name supplied by a user may differ from the denomination stored by INSEE.

Names should therefore be treated as search criteria rather than unique identifiers.

## Multiple results

Search operations may return multiple records.

Do not arbitrarily select one result when several records match.

Use additional information such as:

- location;
- SIREN;
- SIRET;
- legal form;
- activity;
- status;

to distinguish records.

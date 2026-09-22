---
epic: <Epic name>
key: <JIRA-KEY or TBD>
slug: <epic-slug>
product: <product>
intent: intent.md
status: draft
repos: [<affected repos>]
---

# <Epic name> — specification

## Contracts

### API

<Full OpenAPI fragment: paths, schemas, error shapes. Match the conventions
found in TitanWebAPI, as read from the code, not as you would design them.>

### Events

| Event | Payload | Producer | Consumers |
|---|---|---|---|

### Shared types

<The DTOs each client codes against.>

### Data model

<Tables, columns, migrations. Show the existing schema before the change.>

## Behaviour

<Per scenario. Testable. No UI wording.>

## Non-functional

<Only where this change actually moves the needle. Delete if it doesn't.>

## Core dependencies

| What Core must provide | Stub until it lands | Blocking |
|---|---|---|

## Legacy API decisions

<Any WebAPI endpoint in scope: fix in place, or move to TitanWebAPI. One row
per endpoint, with the decision and who made it. Delete if none.>

## Assumptions

- <Every guess made while writing this, listed individually so it can be killed>

## Source references

| Claim | File read |
|---|---|

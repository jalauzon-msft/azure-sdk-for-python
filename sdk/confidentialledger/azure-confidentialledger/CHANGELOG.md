# Release History

## 1.2.0b2 (Unreleased)

### Features Added

### Breaking Changes

### Bugs Fixed

### Other Changes

## 1.2.0b1 (2025-04-23)

### Features Added

- Add and manage custom roles with the `update_user_defined_role`, `get_user_defined_role` and `delete_user_defined_role` methods
- Add and manage ledger users with the `create_or_update_ledger_user`, `delete_ledger_user`, `get_ledger_user` and `list_ledger_users` methods
- Add and manage programmable endpoints with the `create_user_defined_endpoint` and `get_user_defined_endpoint` methods
- A user can now be associated with more than one role
- Added user defined functions support for ledger API

### Other Changes

- A user can now be associated with more than one role
- Replace legacy azure core http response import with the one from azure.core.rest
- Developers should opt to use the `*_ledger_user` methods over the `*_user` methods to manage users. The older APIs will be deprecated in the future.

## 1.1.1 (2023-08-01)

### Bugs Fixed

- Allow some `ResourceNotFoundError` occurrences in `begin_wait_for_commit` to account for unexpected loss of session stickiness. These errors may occur when the connected node changes and transactions have not been fully replicated.

## 1.1.0 (2023-05-09)

### Features Added

- Add `azure.confidentialledger.receipt` module for Azure Confidential Ledger write transaction receipt verification.
- Add `verify_receipt` function to verify write transaction receipts from a receipt JSON object. The function accepts an optional, keyword-only, list of application claims parameter, which can be used to compute the claims digest from the given claims: the verification would fail if the computed digest value does not match the `claimsDigest` value present in the receipt.
- Add `compute_claims_digest` function to compute the claims digest from a list of application claims JSON objects.
- Add sample code to get and verify a write receipt from a running Confidential Ledger instance.
- Update README with examples and documentation for receipt verification and application claims.

### Other Changes

- Add dependency on Python `cryptography` library (`>= 2.1.4`)
- Add tests for receipt verification models and receipt verification public method.
- Add tests for application claims models and digest computation public method.

## 1.0.0 (2022-07-19)

GA Data Plane Python SDK for Confidential Ledger.

### Bugs Fixed

- User ids that are certificate fingerprints are no longer URL-encoded in the request URI.

### Breaking Changes

- Removed all models. Methods now return JSON directly.
- `sub_ledger_id` fields are now named `collection_id`.
- `azure.confidentialledger.identity_service` has been renamed to `azure.confidentialledger.certificate`.
- `ConfidentialLedgerIdentityServiceClient` is now `ConfidentialLedgerCertificateClient`.
- `post_ledger_entry` has been renamed to `create_ledger_entry`.

### Other Changes

- Python 2.7 is no longer supported. Please use Python version 3.7 or later.
- Convenience poller methods added for certain long-running operations.
- Add new supported API version: `2022-05-13`.

## 1.0.0b1 (2021-05-12)

- This is the initial release of the Azure Confidential Ledger library.

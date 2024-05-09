---
title: Auth
date: 2023-08-15T07:30:00-03:00
aliases:
  - /anotacoes/auth0
---
- https://github.com/ory/keto - the first and most popular open source implementation of "Zanzibar: Google's Consistent, Global Authorization System"
- [Stop overloading JWTs with permission claims](https://sdoxsee.github.io/blog/2020/01/06/stop-overloading-jwts-with-permission-claims.html)
- https://auth0.com/blog/on-the-nature-of-oauth2-scopes/
- [SuperTokens](https://supertokens.com/) - #OpenSource User Authentication


## Auth0
- [Get Access Tokens Manually](https://auth0.com/docs/secure/tokens/access-tokens/get-management-api-access-tokens-for-testing#get-access-tokens-manually)
- [Customize prompts API](https://auth0.com/docs/api/management/v2/#!/Prompts/get_prompts)

### Multi-tenancy
- [Multi-Tenant Applications Best Practices](https://auth0.com/docs/get-started/auth0-overview/create-tenants/multi-tenant-apps-best-practices)
#### Organizations
- [Understand How Auth0 Organizations Work](https://auth0.com/docs/manage-users/organizations/organizations-overview)
- [Create Your First Organization](https://auth0.com/docs/manage-users/organizations/create-first-organization)
- [Use Organization Names in Authentication API](https://auth0.com/docs/manage-users/organizations/configure-organizations/use-org-name-authentication-api)

### Refresh Tokens
- allow_offline_access
	- If enabled, Auth0 will allow applications (SPAs) to ask for Refresh Tokens for this API (Servers).
	- "You must enable offline access and request the offline access scope in the client SDK." from https://auth0.com/docs/secure/tokens/refresh-tokens/refresh-token-rotation
- useRefreshTokensFallback
	- [API Reference](https://auth0.github.io/auth0-spa-js/interfaces/Auth0ClientOptions.html#useRefreshTokensFallback)


## JWT
- [jwt.io](https://jwt.io/)
- [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)

### Registered Claims
| Claim | Stands to       | Type                            | Description                           |
| ----- | --------------- | ------------------------------- | ------------------------------------- |
| `iss` | Issuer          | case-sensitive string           | who created and signed this token     |
| `sub` | Subject         | case-sensitive string           | whom the token refers to              |
| `aud` | Audience        | array of case-sensitive strings | who or what the token is intended for |
| `exp` | Expiration Time | number containing a NumericDate |                                       |
| `nbf` | Not Before      | number containing a NumericDate |                                       |
| `iat` | Issued At       | number containing a NumericDate |                                       |
| `jti` | JWT ID          | case-sensitive string           |                                       |


## OAuth2
- [IETF - OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)
- [IETF - OAuth 2.0 for Browser-Based Apps](https://datatracker.ietf.org/doc/draft-ietf-oauth-browser-based-apps/)
- [IETF - RFC 6749 - The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
- [The False Identifier Anti-pattern](https://techcommunity.microsoft.com/t5/microsoft-entra-blog/the-false-identifier-anti-pattern/ba-p/3846013) - use of claims other than subject (`sub`) to uniquely identify an user
- https://oauth.net/2/
- https://swagger.io/docs/specification/authentication/oauth2/

### OpenID Connect
OpenID Connect (OIDC) is an identity layer built on top of the OAuth 2.0.
- https://openid.net/developers/how-connect-works/
- https://swagger.io/docs/specification/authentication/openid-connect-discovery/


## Session
- [IETF - RFC6265 - HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265.html)

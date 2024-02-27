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

### Refresh Tokens
- allow_offline_access
	- If enabled, Auth0 will allow applications (SPAs) to ask for Refresh Tokens for this API (Servers).
	- "You must enable offline access and request the offline access scope in the client SDK." from https://auth0.com/docs/secure/tokens/refresh-tokens/refresh-token-rotation
- useRefreshTokensFallback
	- [API Reference](https://auth0.github.io/auth0-spa-js/interfaces/Auth0ClientOptions.html#useRefreshTokensFallback)
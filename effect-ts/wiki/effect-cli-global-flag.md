---
title: GlobalFlag (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# GlobalFlag (unstable)

Defines flags that apply to every command in a tree, split into two kinds: `Action` flags (side effect then exit — e.g. `--help`, `--version`, `--completions`) and `Setting` flags (values injected into the handler context — e.g. `--log-level`, `--config`). Bundled as built-ins and also extensible.

## Key Exports
- `GlobalFlag<A>` — `Action<A> | Setting<Id, A>` discriminated union
- `Action<A>` — `{ _tag: "Action", flag, run }` side-effect+exit variant
- `Setting<Id, A>` — `{ _tag: "Setting", id, flag }` configures handler context
- `HandlerContext` — info passed to `Action.run` (command, commandPath, version)
- `action` — constructs an `Action` global flag
- `setting` — constructs a `Setting` global flag with an `Id`
- `helpFlag`, `versionFlag`, `completionsFlag` — built-in action flags
- `logLevelFlag` — built-in setting flag providing `LogLevel`
- Used internally by `Command.run` to intercept global concerns before handler invocation

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/GlobalFlag.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-command]]
- [[effect-cli-flag]]

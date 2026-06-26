# Multi-Path Design Checklist

C-end page design must cover all five path categories before a design is considered complete. Use this checklist for design review and prototype design tasks.

Output the coverage status in a design review: which paths are covered in the design, which are missing.

---

## Category 1: Entry Paths — How does the user arrive?

Every C-end page can be reached through multiple entry points. Each entry carries different context, state, and user expectations.

| Entry Type | Description | Coverage |
|---|---|---|
| In-app navigation (Tab / menu) | Normal tap entry; full context available | Required |
| Push notification / deep link | Cold start; may skip navigation context | Required |
| Share link / H5 external link | May be unauthenticated or token-expired | Required |
| Cross-page navigation with params | Arrives with filters, task IDs, or pre-selected state | Required if applicable |
| Back navigation / history | Returns from a child page; state must be restored | Required |

**Common failures**:
- Deep link opens to a page that assumes the user is already in the app flow (broken state)
- Share link doesn't handle unauthenticated users (crash or blank screen)
- Back navigation resets all user input instead of restoring it

---

## Category 2: User State Paths — Who is the user?

The same page behaves differently for different user states. Each must be designed explicitly.

| User State | Description | Coverage |
|---|---|---|
| Not logged in | Redirect to login or show guest mode — must not crash | Required |
| New user (first visit) | Onboarding copy / empty state guidance | Required |
| Returning user (no data) | Historical data cleared, feature newly launched, edge case | Required |
| Insufficient permissions | Feature not activated, tier too low, KYC incomplete | Required |
| Abnormal account | Risk control flag, balance insufficient, account suspended | Required |

**Common failures**:
- New user sees the same empty state as a returning user with cleared data (different contexts need different copy)
- Permission-blocked users see a generic error instead of a clear explanation and upgrade path
- Abnormal account states crash or show untranslated technical errors

---

## Category 3: Data State Paths — What's on the page?

Every data region on the page must handle four states. Never design only the "has data" state.

| State | Requirement |
|---|---|
| Loading | Skeleton / loading placeholder. Must match the final layout to prevent layout shift. |
| Has data (normal) | Primary flow, complete and functional. |
| Empty state | Copy that explains the context + one actionable next step. Never just "暂无数据" / "No data". |
| Error / timeout | Error message that explains what happened + retry button. |

**Common failures**:
- Skeleton layout doesn't match the loaded state (jarring transition)
- Empty state shows "暂无数据" with no guidance on what to do
- Error state has no retry button; user must manually refresh
- Loading state is just a spinner with no layout scaffolding (high reflow on load)

---

## Category 4: Interaction Flow Paths — What does the user do?

The primary flow is never the only flow. Design all four.

| Flow | Description | Coverage |
|---|---|---|
| Happy path | Shortest path to complete the primary goal | Required |
| Interrupted and returned | User left mid-flow and returns; must restore state | Required |
| Repeated action | Double-tap, double-submit, double-confirm — debounce / idempotency | Required |
| Failed action rollback | After a failure, the UI must return to a consistent state | Required |
| Cross-device / cross-platform | Same feature on App and H5 must behave consistently | Required if cross-platform |

**Common failures**:
- User abandons a multi-step form, returns via back button, all fields cleared
- Double-tap on submit creates two orders (no debounce)
- Failed payment leaves the cart in an ambiguous state
- App behavior and H5 behavior diverge on the same feature

---

## Category 5: Environment and Degraded Paths — What if conditions aren't ideal?

| Condition | Requirement |
|---|---|
| Slow / no network | Critical actions must show offline notice and retry. Must not crash. |
| Older app version | Unknown fields and unknown types must degrade gracefully (hide, not crash). |
| Dark mode | Color variables must follow system dark mode; no hardcoded light-mode colors. |
| Small screen / landscape | Layout must adapt; no overflow, no obscured content. |

**Common failures**:
- Slow network shows a blank page with no explanation
- Older app version receives a new field type it doesn't recognize and crashes
- Dark mode renders white text on white background (hardcoded colors)
- Small screen cuts off the primary CTA button

---

## Output format for design reviews

When reviewing a design against this checklist, output:

```
## 多路径覆盖检查

| 路径类型 | 覆盖情况 | 备注 |
|---|---|---|
| 入口路径 | ✅ 已覆盖 / ⚠️ 部分覆盖 / ❌ 未覆盖 | 缺少 deep link 场景 |
| 用户状态 | ✅ / ⚠️ / ❌ | 权限不足状态未设计 |
| 数据状态 | ✅ / ⚠️ / ❌ | 缺少空状态引导动作 |
| 交互流程 | ✅ / ⚠️ / ❌ | 重复提交未处理 |
| 环境降级 | ✅ / ⚠️ / ❌ | 断网场景未覆盖 |

**待补充**：[具体缺失项清单]
```

# Character Customization Guide - Shady Pines

This guide helps you tailor the Shady Pines residents to your specific friends without breaking the "Mystery Engine" (the logic required to solve the crime).

---

## 🟢 Category 1: Total Freedom (Change Anything!)
*These elements are pure flavor and have no impact on the solution.*

| Element | Customization Ideas |
|:---|:---|
| **Character Name** | Use your friend's name or a nickname (e.g., "Auntie Mo"). |
| **Quirks** | Instead of falling asleep, they could be obsessed with a specific TV show, a type of tea, or a pet. |
| **Catchphrases** | Give them a signature line they have to say every 10 minutes. |
| **Wardrobe** | Tell them exactly what to wear (e.g., "Must wear a floral tracksuit"). |
| **History** | Change their past occupation context (e.g., change "Banker" to "Casino Owner"). |

---

## 🟡 Category 2: Careful Tweaks (Change with Caution)
*You can change the flavor, but the core 'vibe' must stay the same.*

| Element | Why it Matters |
|:---|:---|
| **Relationships** | If the General and Sophia have a "treaty," make sure their replacements still have a reason to talk to each other. |
| **Secret Objectives** | You can change the *goal*, but it should still encourage them to move around the facility (e.g., "Find the missing BINGO card" vs "Find the stolen dentures"). |
| **Past Occupation** | It can be anything as long as it explains why they have a specific skill (e.g., a "Detective" needs a reason to be snoopy). |

---

## 🔴 Category 3: Protected Data (DO NOT CHANGE)
*These are the 'gears' of the mystery. Changing these makes the game unsolvable.*

| Element | The Requirement |
|:---|:---|
| **## Clue** | The specific **Location** and **Item** mentioned in the "What they know" section must stay exactly the same. |
| **## Motive** | They must have a reason to dislike the victim (even if you change the *reason*, there must be a 'grudge'). |
| **## Hidden Evidence** | The **Evidence Item** and its **Find Location** must match what is written in the [Master Reveal Matrix](../host/master_reveal_matrix.md). |

---

## 🚀 How to Sync Your Changes
If you update a file in the `characters/` folder, run the following command to make sure your **Public Guest Portal** is updated with the new quirks:

```bash
python generate_public_dossiers.py
```

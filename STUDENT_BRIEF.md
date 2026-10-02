# Student project brief

## Objective

Transform the baseline economy into a small agent-based model addressing a
question chosen by your group.

## Before coding

Complete the following statements:

- **Research question:**
- **Agents:**
- **Main individual states:**
- **Source of heterogeneity:**
- **Information available to agents:**
- **Decision rule:**
- **Interaction mechanism:**
- **What changes or evolves:**
- **Main observable outcome:**
- **Empirical or theoretical reference:**

## Minimum extension

Your model must introduce:

1. one theoretically justified change to agent behaviour;
2. one source of heterogeneity or structured interaction;
3. one experiment comparing a baseline and an alternative scenario;
4. one graph showing how or why the outcomes differ;
5. a short explanation of the mechanism producing the result.

The assessment concerns the coherence between the question, theory, code and
interpretation. A more complicated model is not automatically a better model.

## Recommended workflow

1. Run the unchanged baseline and preserve its outputs.
2. Identify the equation, state variable or interaction protocol to change.
3. Change only one mechanism at first.
4. Add or update a test for that mechanism.
5. Run the modified model with the same random seed.
6. Compare baseline and modified outputs.
7. Explain the causal sequence producing the difference.

Do not place new economic equations directly inside `scheduler.py`. Create a
new file in `equations/`, then import and call it from the scheduler. Place a
matching, trading or rationing procedure in `markets/`.

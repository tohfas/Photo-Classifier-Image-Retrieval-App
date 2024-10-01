# Classification of Prompts by Granularity

Let's classify the prompts used to get outputs based on **granularity levels** and **types** to demonstrate the level of accuracy or detail you're trying to capture in each prompt. We'll categorise the prompt types based on how specific or broad the description is.


## **Prompt Type 1:**
These are generally **broad descriptions**, indicating that the prompt is about categories of players or sports without going into fine details. The **specificity increases** as we move from a general category to specific sports.

1. **Granularity Level 1: Broad Category**
   - *players playing sports* → A general description, covering all types of sports.

2. **Granularity Level 2: Specific Sport**
   - *players playing football* → A more specific description, focusing on **football**.

3. **Granularity Level 2: Specific Sport**
   - *players playing hockey* → Similarly specific, but focusing on **hockey**.



## **Prompt Type 2:**
This type progressively adds details to describe **flowers** with increasing specificity, moving from a general description of flowers to specific types and their colors.

1. **Granularity Level 1: General Category**
   - *Flowers in the garden* → A broad description of flowers in a garden setting.

2. **Granularity Level 2: Specific Type**
   - *Flowers in the garden that are roses* → More specific, limiting the search to **roses**.

3. **Granularity Level 2: Specific Type**
   - *Flowers in the garden that are tulips* → Similar to the above but focusing on **tulips**.

4. **Granularity Level 3: Specific Type with Attribute**
   - *Flowers in the garden that are red tulips* → The most specific, focusing on **red tulips**, which combines both type and color.


## **Prompt Type 3: People Holding Cameras**
These prompts are about **actions or objects** associated with people, focusing on an activity (holding a camera) and refining based on gender.

1. **Granularity Level 1: General Category with Object**
   - *people having a camera in hand* → A general description of people with cameras, no gender specification.

2. **Granularity Level 2: Specific Gender**
   - *women having a camera in hand* → More specific, narrowing the focus to **women** holding cameras.


## **Prompt Type 4:**
This type describes **roles and specific attributes** related to nurses, moving from a general description of nurses to more specific details like wearing masks.

1. **Granularity Level 1: Role Identification**
   - *Picture of nurse* → A general description, identifying a **nurse**.

2. **Granularity Level 2: Role with Attribute**
   - *nurse with mask on faces* → A more specific description requiring recognition of **nurses** wearing **masks**.


## **Summary of Granularity Levels and Accuracy Goals:**
- **Granularity Level 1 (Broad Category)**: General identification (e.g., *players*, *flowers in a garden*, *people*). This requires recognising broad categories with a lower level of specificity.
- **Granularity Level 2 (Specific Category or Attribute)**: Specific identification within a category (e.g., *football players*, *roses*, *women*). This focuses on accurate identification of subcategories or attributes.
- **Granularity Level 3 (Very Specific Detail or Attribute)**: Highly detailed prompts (e.g., *red tulips*, *nurses with masks*). The highest level of accuracy is needed to capture both the object or person and their specific attributes.

As the prompts become more detailed, the accuracy expectations increase. The model needs to identify both the **broader category** (e.g., *players*, *flowers*, *people*) and correctly capture **specific details** (e.g., *football*, *roses*, *gender*, *mask*).

Our developed product can successfully provide images with this level of granularity provided images are of high quality, number of relevant images during traing are adequate and good to have more, and prompt should be of high quality.

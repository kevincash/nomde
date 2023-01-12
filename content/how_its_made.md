Title: How It's Made
Tags: pelican, python
Slug: how-its-made
Date: 2023-01-10
Summary: Read on for a description of the neat tech that serves up this site.
Author: Kevin Cash

This site partially exists as an excuse to learn about front-end development, something I have only a beginner's knowledge of.

A few years ago, I remember a good friend of mine — the venerable Joe Trubenstein — wouldn't stop talking about static sites. He was particularly obsessed with Jamstack and Gatsby.

I sort of fooled around with that, throwing together a site with a headless CMS (Ghost). It was damn easy and, as I was sold on, lightning fast. 

At the time, I was interested in churning out content sites that I could run ads on. I'd had a lot of experience writing content on competitive subject matters (mostly personal finance) and thought, "Hey -- I need a piece of this pie!"

I started a site focused on pet health, wrote two articles, and... yada, yada, yada... was reminded of the site's existence a year later with a namecheap domain renewal email.

I'm fairly convinced that, at this point in my life, any business I start should fit one primary criteria: I've got to _really_ be interested in the subject matter and not be just pursuing out of pure profit interests.

But wait -- wasn't _this_ article supposed to be about how _this_ site was built and not your boring endless ramblings? Yes. Back on track.

## Pelican: a static site generator for Python

This site is built entirely using Pelican, a pretty nifty/ relatively easy to use static site generator written entirely in Python.

### How it works

All of my articles, pages, etc. on this site are initially written in markdown. "All" includes not only the actually content of the pages, but also metadata like:

- Article title
- Summary
- Date
- Slug
- Tags
- Category

... and more. Really, if there's any data you want to incorporate into an article, you can assign a field 

I like to think about Pelican (and I suppose this applies to other site generators, static and dynamic) using a cooking metaphor.

Let's consider a markdown document to be our ingredients and quantities -- for grilled cheese.

| Ingredient      | Quantity |
| ----------- | ----------- |
| bread       | 2 slices       |
| butter      | 1/2 tbsp        |
| american cheese      | 1 slice       |
| tomatoes    | 2 slices        |

**Grilled cheese ingredients:**

- 2 slices bread
- 1/2 tbsp butter
- 1 slice american cheese
- 2 slices tomatoes

**Markdown:**

- Metadata 

In this case, the *ingredients* (bread, butter, cheese, tomatoes) are equivalent to markdown's written content — that is, the actual words to be displayed.

We'll consider the quantities (2, 1/2, 1, 2) equivalent to markdown's formatting instructions (e.g. which text should be bolded, italicized, formatted as an H2, H3... what text represents the article's meta summary, url slug, title, etc).

Markdown formatting, for all intents, is simply:

- a **higher-level** abstration of HTML/ CSS
- a **lower-level** abstraction of a WYSIWYG editor

For those of us that demand more control than a CMS affords, but don't want to waste away writing the same HTML/ CSS over and over again, writing in markdown represents a fine solution. It exists as an embodiment of an essential principal of software development: Do Not Repeat Yourself (DRY).

All article pages on a blog are going to be _mostly_ the same. What, then, will distinguish one from another?

- the title
- the content (the headers, the body paragraphs)
- the url slug
- the summary

... and some other stuff.

So, really, a templating system (Jinja2 in this case) separates how we define:

- the style of _a page_, and
- that page's _content_ and _metadata_ (in addition to some content styling, like **bolding** and **italizing**)

Separating these two groups of definitions saves an enormous amount of time that might otherwise be spent writing boilerplate code and mapping that code to the written content we want its style and function to be defined by.

The recipe alone has _most_ of the details we need to make chicken marsala. It provides all the ingredients (attributes) and instructions (methods) on how to turn those ingredients into a delicious meal.

Unfortunately, we won't receive the same satisfaction from eating the paper the recipe is printed on as we might eating the actual prepared meal.

So, there exists a gap between printed recipes _and_ delicious chicken marsala meal!

There exists a gap between markdown (written word with _some_ instructions on how they should be formatted)_and_ that page served in a beautifully formatted way that exists as _a part_ of a whole website.

Pelican, relying heavily on the Jinja2 templating language, fills this gap. Here's how:

1. Write some article in markdown.
2. Write some instructions on how the content of that article should be interpreted/ converted into HTML/ CSS.
3. Write some instructions on how that article should be organized in the context of a multi-paged website _and_ where it should be published.

There are a lot of (free!) packages/ tools beyond Pelican, Python and Jinja2 that enable this complex dance, but most of them are abstracted away.


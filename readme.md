# Deta Community Faq

Community managed faq for the [deta](https://deta.space) platform

## Adding an faq page

Create a new html file in the `/templates/faq` folder and make it then next number from the one before _(so if the current highest number is 6 make yours 7)_

The basic structure of the html should look something like this

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Faq</title>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" href="/static/images/icon.png" type="image/x-icon" />
    <link rel="stylesheet" href="/static/styles/style.css" />
    <link rel="stylesheet" href="/static/styles/command.css" />

    <meta property="og:image" content="/static/images/icon.png" />
    <meta property="og:description" content="Read more..." />
    <meta name="url" content="https://faq.deta.dev/" />
    <meta property="og:title" content="FAQ TITLE HERE" />
    <meta property="og:type" content="website" />
    <meta name="theme-color" content="#F73A95" />
  </head>

  <body>
    <div class="container">
      <div class="title">
        <a href="/" style="text-decoration: none;">←</a> FAQ TITLE HERE bot?
      </div>
      <div class="content">
        <div class="content-text">
          Qui consequatur est magni eum eum voluptas unde dignissimos. Quia
          perferendis est sequi alias. Quia adipisci quam velit voluptatum vero
          laboriosam quia. Dolor deleniti aut nemo. Eum neque eum voluptate ex
          perferendis.
        </div>
        <div class="content-text">
          Ipsa sint cupiditate qui voluptatem sint. Odit quis eos omnis neque ab
          eos ea eius. Magni necessitatibus impedit voluptatem et necessitatibus
          neque est soluta. Quaerat et eum et vel sit suscipit consequuntur
          commodi. Aut ab in et sed suscipit ex ut quisquam.
        </div>
      </div>
      <div class="bottom">
        <a href="https://github.com/SlumberDemon/faqs">Source</a> /
        <a href="https://github.com/SlumberDemon/faqs/{{ page }}">Edit</a>
      </div>
    </div>
  </body>
</html>
```

You can use the `content-text` for a new paragraph on the page. If you want to use links use `<a>` tags like this make sure to leave spaces behind and infront of the `<a>` tag so its not attached to other text

```html
<a href="https://linktopagehere">text</a>
```

## Disclaimer

> This website is not affiliated with deta

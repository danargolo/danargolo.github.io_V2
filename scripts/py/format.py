def format_header(config, content, style):
  return(
    f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{config['title']}</title>
  <script src=""></script>
  <link rel="stylesheet" href="/styles/global.css">
  <link rel="stylesheet" href="/styles/{style['page']}.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
      </ul>
    </nav>  
  </header>
  <main>
    <div class="container">
      <section class={style['class']}>
        <div class="title">
          <p id="title">{config['title']}</p>
          <p id="subtitle">{config['description']}</p>
        </div>
        {content}
      </section>
      <aside style="display: flex; justify-content: right;">
        <img style="border: 2px solid rgb(233, 234, 240);" src="" alt="">
        <div id="card">
          <h3>{config['author']}</h3>
          <h5>{config['occupation']}</h5>
          <ul id="link">
            <li><a href="{config['links']['github']}" target="_blank">Github</a></li>
            <li><a href="{config['links']['linkedin']}" target="_blank">Linkedin</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </main>
  <footer>
    <p>{config['message_footer']}</p>
  </footer>
</body>
</html>"""
  )
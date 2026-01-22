<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Himalayan IT College</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, Helvetica, sans-serif;
    }

    body {
      height: 100vh;
    }

    .hero {
      height: 100vh;
      background-image:
        linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url("himalayan.jpg");
      background-size: cover;
      background-position: center;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
    }

    .hero-content {
      color: white;
      max-width: 900px;
      padding: 20px;
    }

    .hero-content h1 {
      font-size: 48px;
      margin-bottom: 20px;
    }

    .hero-content p {
      font-size: 18px;
      margin-bottom: 35px;
      line-height: 1.6;
    }

    .btn {
      display: inline-block;
      padding: 14px 30px;
      margin: 0 10px;
      border-radius: 6px;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
    }

    .btn.learn {
      background-color: #3b82f6;
      color: white;
    }

    .btn.visit {
      background-color: #facc15;
      color: black;
    }
  </style>
</head>

<body>

  <section class="hero">
    <div class="hero-content">
      <h1>Enhance Your Future With<br>Himalayan IT College</h1>

      <p>
        Build your career with industry-focused IT courses, hands-on projects,
        and globally recognized certifications.
      </p>

      <a href="#" class="btn learn">Learn More</a>
      <a href="#" class="btn visit">Visit Courses</a>
    </div>
  </section>

</body>
</html>

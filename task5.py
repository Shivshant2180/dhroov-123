
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Social Media Platform</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: space-between;
            background-color: #444;
            padding: 10px;
        }
        nav a {
            color: white;
            padding: 10px;
            text-decoration: none;
        }
        .main-content {
            display: flex;
            flex-wrap: wrap;
        }
        .post {
            background-color: #f9f9f9;
            padding: 20px;
            margin: 10px;
            flex: 1 1 calc(33.333% - 20px);
            box-sizing: border-box;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }
        @media (max-width: 768px) {
            .post {
                flex: 1 1 calc(50% - 20px);
            }
        }
        @media (max-width: 480px) {
            .post {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>My Social Media Platform</h1>
    </header>
    
    <nav>
        <a href="#">Home</a>
        <a href="#">Profile</a>
        <a href="#">Messages</a>
        <a href="#">Settings</a>
    </nav>
    
    <div class="container">
        <div class="main-content">
            <div class="post">Post 1</div>
            <div class="post">Post 2</div>
            <div class="post">Post 3</div>
            <div class="post">Post 4</div>
            <div class="post">Post 5</div>
        </div>
    </div>
    
    <footer>
        <p>© 2024 Social Media Platform</p>
    </footer>

    <script>
        // Add swipe gesture support (JavaScript part)
        let startX;
        document.addEventListener('touchstart', function(e) {
            startX = e.touches[0].pageX;
        });
        
        document.addEventListener('touchmove', function(e) {
            let moveX = e.touches[0].pageX;
            if (startX - moveX > 50) {
                alert('Swiped Left!');
            } else if (moveX - startX > 50) {
                alert('Swiped Right!');
            }
        });
    </script>
</body>
</html>
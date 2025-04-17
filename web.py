# 静态网页生成器
def generate_static_website(output_file="index.html"):
    html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的静态网页</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        
        header {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        nav {
            background-color: #333;
            padding: 1rem 0;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 15px;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            margin-bottom: 2rem;
        }
        
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }
        
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            nav ul li {
                margin: 5px 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>欢迎来到我的网站</h1>
            <p>这是一个使用Python生成的静态网页</p>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="#home">首页</a></li>
                <li><a href="#about">关于</a></li>
                <li><a href="#services">服务</a></li>
                <li><a href="#contact">联系</a></li>
            </ul>
        </div>
    </nav>
    
    <div class="container">
        <section id="home" class="card">
            <h2>首页内容</h2>
            <p>这里是网站的主要内容区域。你可以在这里添加各种内容，如文章、图片、产品展示等。</p>
            <p>使用Python生成静态网页非常简单，只需要将HTML内容写入文件即可。</p>
        </section>
        
        <section id="about" class="card">
            <h2>关于我们</h2>
            <p>我们是一个致力于提供高质量网页模板的团队。我们的目标是让网页开发变得更加简单高效。</p>
        </section>
        
        <section id="services" class="card">
            <h2>我们的服务</h2>
            <ul>
                <li>网页设计与开发</li>
                <li>静态网站生成</li>
                <li>响应式布局</li>
                <li>SEO优化</li>
            </ul>
        </section>
        
        <section id="contact" class="card">
            <h2>联系我们</h2>
            <p>邮箱: contact@example.com</p>
            <p>电话: 123-456-7890</p>
        </section>
    </div>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 我的静态网站. 保留所有权利.</p>
        </div>
    </footer>
</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"静态网页已生成: {output_file}")

# 生成网页
generate_static_website()
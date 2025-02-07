async function loadBlogPosts() {
    try {
        const response = await fetch('posts/posts.json');
        const data = await response.json();
        
        // Check if we're on a single post page or the main blog listing
        const urlParams = new URLSearchParams(window.location.search);
        const postId = urlParams.get('post');
        
        const blogPostsSection = document.querySelector('.blog-posts');
        if (!blogPostsSection) return;

        if (postId) {
            await loadSinglePost(data.posts, postId);
        } else {
            loadPostsList(data.posts);
        }
    } catch (error) {
        console.error('Error loading blog posts:', error);
        const blogPostsSection = document.querySelector('.blog-posts');
        if (blogPostsSection) {
            blogPostsSection.innerHTML = '<p>Error loading blog posts. Please try again later.</p>';
        }
    }
}

function loadPostsList(posts) {
    const blogPostsSection = document.querySelector('.blog-posts');
    if (!blogPostsSection) return;
    
    blogPostsSection.innerHTML = ''; // Clear existing content
    
    posts
        .sort((a, b) => new Date(b.date) - new Date(a.date)) // Sort by date, newest first
        .forEach(post => {
            const article = document.createElement('article');
            article.className = 'post-preview';
            article.innerHTML = `
                <h2>${post.title}</h2>
                <p class="post-date">Geplaatst op ${formatDate(post.date)}</p>
                <div class="post-preview-content">${post.preview}</div>
                <a href="?post=${post.url}" class="read-more">Lees meer</a>
            `;
            blogPostsSection.appendChild(article);
        });
}

async function loadSinglePost(posts, postId) {
    const post = posts.find(p => p.url === postId);
    if (!post || !post.content) {
        window.location.href = 'index.html';
        return;
    }

    const blogPostsSection = document.querySelector('.blog-posts');
    if (!blogPostsSection) return;

    blogPostsSection.innerHTML = `
        <article class="full-post">
            <h1>${post.title}</h1>
            <p class="post-date">Geplaatst op ${formatDate(post.date)}</p>
            <div class="post-content">
                <div class="intro">${post.content.intro}</div>
                ${post.content.sections.map(section => `
                    <section>
                        <h2>${section.title}</h2>
                        ${section.content ? `<p>${section.content}</p>` : ''}
                        ${section.code ? `<pre><code>${section.code}</code></pre>` : ''}
                        ${section.list ? `
                            <ul>
                                ${section.list.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        ` : ''}
                    </section>
                `).join('')}
                <div class="conclusion">${post.content.conclusion}</div>
            </div>
            <a href="index.html" class="back-to-blog">← Terug naar Blog</a>
        </article>
    `;

    // Update page title
    document.title = `${post.title} - WebDev Inzichten`;
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('nl-NL', options);
}

// Load posts when the page loads
document.addEventListener('DOMContentLoaded', loadBlogPosts); 
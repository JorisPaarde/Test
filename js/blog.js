async function loadBlogPosts() {
    try {
        const response = await fetch('../posts/posts.json');
        const data = await response.json();
        
        const blogPostsSection = document.querySelector('.blog-posts');
        blogPostsSection.innerHTML = ''; // Clear existing content
        
        data.posts
            .sort((a, b) => new Date(b.date) - new Date(a.date)) // Sort by date, newest first
            .forEach(post => {
                const article = document.createElement('article');
                article.className = 'post-preview';
                article.innerHTML = `
                    <h2>${post.title}</h2>
                    <p class="post-date">Posted on ${formatDate(post.date)}</p>
                    <p>${post.preview}</p>
                    <a href="posts/${post.url}">Read More</a>
                `;
                blogPostsSection.appendChild(article);
            });
    } catch (error) {
        console.error('Error loading blog posts:', error);
    }
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

// Load posts when the page loads
document.addEventListener('DOMContentLoaded', loadBlogPosts); 
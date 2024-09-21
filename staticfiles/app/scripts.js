let likeCount = 0;
let commentCount = 0;

function toggleMenu() {
  const menu = document.getElementById('menu');
  menu.classList.toggle('show');
}

function likePost() {
  likeCount++;
  document.getElementById('like-count').innerText = likeCount;
}

function postComment() {
  const name = document.getElementById('commenter-name').value;
  const comment = document.getElementById('comment-content').value;

  if (name && comment) {
    const commentList = document.getElementById('comment-list');
    const newComment = document.createElement('div');
    newComment.innerHTML = `<strong>${name}:</strong> <p>${comment}</p>`;
    commentList.appendChild(newComment);

    commentCount++;
    document.getElementById('comment-count').innerText = commentCount;

    document.getElementById('commenter-name').value = '';
    document.getElementById('comment-content').value = '';
  } else {
    alert('Please fill in both name and comment fields.');
  }
}

// Add search functionality
document.getElementById('search-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const query = document.getElementById('search-input').value;
  if (query) {
    alert(`You searched for: ${query}`);
    document.getElementById('search-input').value = ''; // Clear the input
  }
});

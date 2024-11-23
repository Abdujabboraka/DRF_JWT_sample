function toggleComments(index) {
    const commentsSection = document.getElementById(`comments-${index}`);
    if (commentsSection.classList.contains('hidden')) {
        commentsSection.classList.remove('hidden');
    } else {
        commentsSection.classList.add('hidden');
    }
}

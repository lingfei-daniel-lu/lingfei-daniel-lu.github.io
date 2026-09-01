/* Research page: expand/collapse all summaries */
document.addEventListener('DOMContentLoaded', function () {
  var expandButton = document.getElementById('expand-all-summaries');
  var collapseButton = document.getElementById('collapse-all-summaries');
  if (expandButton) {
    expandButton.addEventListener('click', function () {
      document.querySelectorAll('.research-summary').forEach(function (summary) {
        if (!summary.open) {
          summary.open = true;
        }
      });
    });
  }
  if (collapseButton) {
    collapseButton.addEventListener('click', function () {
      document.querySelectorAll('.research-summary').forEach(function (summary) {
        if (summary.open) {
          summary.open = false;
        }
      });
    });
  }
});

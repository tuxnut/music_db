// Display / Hide the forms to add a musicScore / composer
const toggleForm = () => {
    const element = document.getElementById("form");
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

// Filter musicScore by title
const sortByInput = () => {
    const input = document.getElementById("search_bar");
    const filter = input.value.toUpperCase();
    const musicScoreTable = document.getElementById("scoreTable")
    const rows = musicScoreTable.getElementsByTagName("tr")

    // loop through table rows, hide the ones that does not match the input
    for (let i = 0; i < rows.length; ++i) {
        const scoreTitle = rows[i].getElementsByTagName("td")[0];
        if (scoreTitle) {
            let titleValue = scoreTitle.textContent || scoreTitle.innerText;
            if (titleValue.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
    v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
    )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

// Sort the tables by the clicked column - Bubble sort
const sortTable = (column) => {
    const page = document.getElementsByTagName("title")[0].textContent;
    const table = document.getElementById((page === "Partitions") ? "scoreTable" : "composerTable");
    Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
        .sort(comparer(column, this.asc = !this.asc))
        .forEach(tr => table.appendChild(tr) );

}
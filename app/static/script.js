const s_titleColumn          = 1;
const s_composerNameColumn   = 2;
const s_typeColumn           = 3;
const s_creationDateColumn   = 4;
const s_difficultyColumn     = 5;
const s_commentColumn        = 6;

const c_fullNameColum        = 0;
const c_birthColum           = 1;
const c_deathColum           = 2;
const c_nationalityColum     = 3;
const c_styleColum           = 4;

// Filter musicScore by title and or composer
const sortByInput = () => {
    const input = document.getElementById("search_bar");
    const filter = input.value.toUpperCase();
    const musicScoreTable = document.getElementById("scoreTable")
    const rows = musicScoreTable.getElementsByTagName("tr")

    // loop through table rows, hide the ones that does not match the input
    for (let i = 0; i < rows.length; ++i) {
        const scoreTitle = rows[i].getElementsByTagName("td")[s_titleColumn];
        const composerName = rows[i].getElementsByTagName("td")[s_composerNameColumn];
        if (scoreTitle && composerName) {
            let titleValue = scoreTitle.textContent || scoreTitle.innerText;
            let composerNameValue = composerName.textContent || composerName.innerText;
            if ((titleValue.toUpperCase().indexOf(filter) > -1) || (composerNameValue.toUpperCase().indexOf(filter) > -1)) {
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

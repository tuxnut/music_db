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

const handleEditComposer = (serializedItem) => {
    composer = JSON.parse(serializedItem);
    const container = document.getElementById('editionForm');
    
    container.children.namedItem('key').value = composer.commonname;
    container.children.namedItem('name').value = composer.commonname;    
    container.children.namedItem('fullname').value = composer.fullname;
    container.children.namedItem('dateOfBirth').value = composer.dateofbirth;
    container.children.namedItem('dateOfDeath').value = composer.dateofdeath;
    container.children.namedItem('nationality').value = composer.nationality;
    container.children.namedItem('style').value = composer.style;

    document.getElementById('edit').style.display ='block';
}

const handleDeleteComposer = (itemName) => {
    const container = document.getElementById('deletionForm');
    
    container.children.namedItem('namePlaceHolder').textContent = itemName;
    container.children.namedItem('key').value = itemName;

    document.getElementById('delete').style.display ='block';
}

// Get the modals
const modalEdit = document.getElementById('edit');
const modalDelete = document.getElementById('delete');

// When the user clicks anywhere outside of the modals, close it
window.onclick = (event) => {
    if ((event.target == modalEdit) || (event.target == modalDelete)) {
        modal.style.display = "none";
    }
}

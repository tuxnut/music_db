% include('menubar.tpl')

<h1>Partitions</h1>

<!-- Button to toggle the form -->
<button onclick="toggleForm()">Ajouter une partition</button>
<div style="display:none" id="sheetForm">
    % include('sheetForm.tpl', composersArray=composersArray)
</div>
<br>
<hr>
<br>
<div class="containerTable">
    <table id="sheetTable">
        <tr>
            <th>Titre</th>
            <th>Compositeur</th>
            <th>Type</th>
            <th>Date de composition</th>
            <th>Difficulté</th>
            <th>Appréciation</th>
            <th>Commentaires</th>
        </tr>
        % for item in musicSheetsArray:
            <tr>
                <td>{{item['title']}}</td>
                <td>{{item['commonname']}}</td>
                <td>{{item['type']}}</td>
                <td>{{item['dateofcreation']}}</td>
                <td>{{item['difficulty']}}</td>
                <td>{{item['appreciation']}}</td>
                <td>{{item['comments']}}</td>
            </tr>
        % end
    </table>
</div>

<script>
    function toggleForm() {
        const element = document.getElementById("sheetForm");
        if (element.style.display === "none") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }
</script>

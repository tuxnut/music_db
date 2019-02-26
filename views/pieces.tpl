% include('menubar.tpl')

<h1>Partitions</h1>

<!-- Button to hide the form by default -->
<button onclick="toggleForm()">Ajouter une partition</button>
<div style="display:none" id="pieceForm">
    % include('pieceForm.tpl', composersArray=composersArray)
</div>
<br>
<hr>
<br>
<div class="containerTable">
    <table id="pieceTable">
        <tr>
            <th>Titre</th>
            <th>Compositeur</th>
            <th>Type</th>
            <th>Date de composition</th>
            <th>Difficulté</th>
            <th>Appréciation</th>
            <th>Commentaires</th>
        </tr>
        % for item in piecesArray:
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
        const element = document.getElementById("pieceForm");
        if (element.style.display === "none") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }
</script>
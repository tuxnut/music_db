<!DOCTYPE html>
<html>
<head>
    <title>Partitions</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    % include('menubar.tpl')

    <h1>Partitions</h1>

    <input type="text" id="search_bar" name="search" placeholder="Search.." oninput="sortByInput()"><br>

    <!-- Button to toggle the form -->
    <button onclick="toggleForm()" id="toggleFormButton"><span>Ajouter une partition</span></button>
    <div style="display:none" id="form" class="formContainer">
        % include('scoreForm.tpl', composersArray=composersArray)
    </div>
    <br>
    <br>
    <div class="containerTable">
        <table id="scoreTable">
            <tr>
                <th onclick="sortTable(0)">Titre</th>
                <th onclick="sortTable(1)">Compositeur</th>
                <th onclick="sortTable(2)">Type</th>
                <th onclick="sortTable(3)">Date de composition</th>
                <th onclick="sortTable(4)">Difficulté</th>
                <th onclick="sortTable(5)">Appréciation</th>
                <th onclick="sortTable(6)">Commentaires</th>
            </tr>
            % for item in musicScoresArray:
            <tr>
                <td>{{item['title']}}</td>
                <td>{{item['composer']['commonname']}}</td>
                <td>{{item['type']}}</td>
                <td>{{item['dateofcreation']}}</td>
                <td>{{item['difficulty']}}</td>
                <td>{{item['appreciation']}}</td>
                <td>{{item['comments']}}</td>
            </tr>
            % end
        </table>
    </div>

    <script src="script.js"></script>

</body>
</html>

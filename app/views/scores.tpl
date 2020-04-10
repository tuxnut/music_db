% from DatabaseService import computeScorePresence

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
    <br>
    <div class="containerTable">
        <table id="scoreTable">
            <tr>
                <th></th>
                <th class="clickable" onclick="sortTable(1)">Titre</th>
                <th class="clickable" onclick="sortTableByFamilyName(2)">Compositeur</th>
                <th class="clickable" onclick="sortTable(3)">Type</th>
                <th class="clickable" onclick="sortTable(4)">Date de composition</th>
                <th class="clickable" onclick="sortTable(5)">Difficulté</th>
                <th class="clickable" onclick="sortTable(6)">Commentaires</th>
            </tr>
            % for item in musicScoresArray:
            <tr>
                <td>
                % for score in computeScorePresence(item['score_id'], item['title'], item['composer']['commonname']):
                    <a href="sheets/web/viewer.html?file=../{{score}}" rel="noopener" target="_blank">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><path d="M15 6H3v2h12V6zm0 4H3v2h12v-2zM3 16h8v-2H3v2zM17 6v8.18c-.31-.11-.65-.18-1-.18-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3V8h3V6h-5z"/></svg>
                    </a>
                % end
                </td>
                <td>{{item['title']}}</td>
                <td>{{item['composer']['commonname']}}</td>
                <td>{{item['type']}}</td>
                <td>{{item['dateofcreation']}}</td>
                <td>{{item['difficulty']}}</td>
                <td>{{item['comments']}}</td>
            </tr>
            % end
        </table>
    </div>
    <script src="script.js"></script>
</body>
</html>

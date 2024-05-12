var kurs_id = {}; // Global o'zgaruvchi
function showKurs(select) {
    var selectedFakul = select.value;
    var kursSelect = document.getElementById("kurs_id");

    switch(selectedFakul) {
        case '6':  // +
        case '4':
            kursSelect.innerHTML =  "<option value='1-kurs'>1-kurs</option>" +
                                    "<option value='2-kurs'>2-kurs</option>" +
                                    "<option value='3-kurs'>3-kurs</option>" +
                                   "<option value='4-kurs'>4-kurs</option>" +
                                   "<option value='5-kurs'>5-kurs</option>" +
                                   "<option value='6-kurs'>6-kurs</option>";
            break;
        case '10':
        case '115':
        case '9':
        case '11':
        case '1':
        case '5':
        case '226':
        case '7':
            kursSelect.innerHTML = "<option value='1-kurs'>1-kurs</option>" +
                                   "<option value='2-kurs'>2-kurs</option>" +
                                   "<option value='3-kurs'>3-kurs</option>" +
                                   "<option value='4-kurs'>4-kurs</option>" +
                                   "<option value='5-kurs'>5-kurs</option>" +
                                   "<option value='6-kurs'>6-kurs</option>";
            break;
        default:
            kursSelect.innerHTML = "<option selected disabled>Kursni tanglang ...</option>"; // Fakultet tanlanmaganida sukutda bo'lishi
            break;
    }
}
function showGroups(select) {
var selectedFakul = document.getElementById("fakul_id").value;
var selectedKurs = select.value;
var groupSelect = document.getElementById("group_select");
groupSelect.innerHTML = ""; // Avvalgi tanlovni o'chirish

switch(selectedFakul) {
    case '6':
        if (selectedKurs === '1-kurs') {
            {% for x in groups %}
                {% if "st2023" in x.name and "qtst2023" not in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '2-kurs') {
            {% for x in groups %}
                {% if "st2022" in x.name and "qtst2022" not in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }

        if (selectedKurs === '3-kurs') {
            {% for x in groups %}
                 {% if "st2021" in x.name and "qtst2021" not in x.name  and "xtst2021" not in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '4-kurs') {
            {% for x in groups %}
                {% if "st2020" in x.name or "stbds2020" in x.name %}
                     {% if "qtst2020" not in x.name and "xtst2020" not in x.name %}
                        groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                    {% endif %}
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '5-kurs') {
            {% for x in groups %}
                 {% if "st2019" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        break;
    case '4':
        if (selectedKurs === '1-kurs') {
            {% for x in groups %}
                {% if "pf2023" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '2-kurs') {
            {% for x in groups %}
                 {% if "pf2022" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }

        if (selectedKurs === '3-kurs') {
            {% for x in groups %}
                 {% if "pf2021" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '4-kurs') {
            {% for x in groups %}
                {% if "pf2020" in x.name %}
                        groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        if (selectedKurs === '5-kurs') {
            {% for x in groups %}
                {% if "pf2019-" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
         if (selectedKurs === '6-kurs') {
            {% for x in groups %}
                  {% if "pf2018-" in x.name %}
                    groupSelect.add(new Option("{{ x.name }}", "{{ x.id }}"));
                {% endif %}
            {% endfor %}
        }
        break;
}
}

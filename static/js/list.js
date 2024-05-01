$(document).ready(function() {

    $('#person-search').on('click', function () {
        var search = $('#person-search-value').val();
        var lang = 'uz-UZ';
        var personType = 'teacher';
        var passNumber = $('#person-number-value').val();
        if (personType == 'student') {
            var url = 'https://sammu.uz/frontend/web/profile/get-student-data';
        } else if (personType == 'teacher') {
            var url = '/uz/profile/get-student-data';
        }

        if (search.length >= 13 && passNumber.length >= 5) {
            $.ajax({
                url: url,
                method: 'GET',
                data: {
                    search: search,
                    pass: passNumber,
                    lang: lang,
                },
                success: function (data) {
                    var text = '';
                    if (data.success == true && data.data.items[0]) {
                        var b = 0;
                        for (var i = 0; i < data.data.items.length; i++) {
                            if (data.data.items[i].image) {
                                var img = data.data.items[i].image;
                            } else {
                                var img = 'https://via.placeholder.com/150';
                            }
                            text += '<div class="search-item"><div class="row">';
                            text += '<div class="col-md-1 search-img-custom"><img src="' + img +'" alt="" class="img-fluid" style="height: auto;"></div>';
                            text += '<div class="col-md-11"><div class="row search-info-custom"><div class="col-md-3"><div class="contact-form"><label>F.I.O.</label>';
                            text += '<input type="text" class="form-control" value="' + data.data.items[i].full_name + '" disabled></div></div>';
                            text += '<div class="col-md-3"><div class="contact-form"><label>Kafedra / Bo\'lim</label>';
                            text += '<input type="text" class="form-control" value="' + data.data.items[i].department.name + '" disabled></div></div>';
                            text += '<div class="col-md-3"><div class="contact-form"><label>Lavozim</label>';
                            if (personType == 'student') {
                                text += '<input type="text" class="form-control" value="' + data.data.items[i].level.name + ' ' + data.data.items[i].group.name + '" disabled></div></div>';
                                text += '<div class="col-md-3"><div class="contact-form" style="padding-top: 37px;"><button type="button" class="btn btn-outline-success btn-block btn-lg" id="select-student-button" data-id="' + data.data.items[i].student_id_number +'">Tanlash</button></div></div>';
                            } else if (personType == 'teacher') {
                                text += '<input type="text" class="form-control" value="' + data.data.items[i].staffPosition.name + '" disabled></div></div>';
                                text += '<div class="col-md-3"><div class="contact-form" style="padding-top: 37px;"><button type="button" class="btn btn-lg btn-primary" id="select-student-button" data-id="' + data.data.items[i].employee_id_number +'" data-item="' + b + '">Tanlash</button></div></div>';
                            }
                            text += '</div></div></div></div>';
                            b++;
                        }
                        $('#search-result').html(text);
                        $('#search-result').show();
                    } else {
                        $('#search-result').show();
                        $('#search-result').html('<div class="search-item"><div class="row"><div class="col-md-12 text-center"><div class="form-group p-3"><label>Ma\'lumot topilmadi!</label></div></div></div></div>');
                    }
                },
            });
        } else {
            alert('PINFL hamda pasport seriyasi va raqami to\'ldirilishi lozim');
        }
    });

    $(document).on('click', '#select-student-button', function () {
        var student_id = $(this).data('id');
        var item = $(this).data('item');
        var personType = 'teacher';
        $('#search-result').hide();
        selectPerson(student_id, personType, item);
        $('#user-passport_info').val($('#person-number-value').val());
        $('#user-pin').val($('#person-search-value').val());


        $('#input-user-passport_info:disabled').val($('#person-number-value').val());
        $('#input-user-pin:disabled').val($('#person-search-value').val());

    });

    function selectPerson(person_id, type, item) {
        if (type == 'student') {
            $.ajax({
                url: 'https://sammu.uz/frontend/web/profile/get-student-data',
                method: 'GET',
                data: {
                    search: person_id,
                    lang: 'uz-UZ',
                },
                success: function (data) {
                    if (data.success == true && data.data.items[0]) {
                        $('#person-person_id').val(data.data.items[0].student_id_number);
                        $('#person-image').val(data.data.items[0].image);
                        $('#person-full_name').val(data.data.items[0].full_name);
                        $('#person-department_faculty').val(data.data.items[0].department.name);
                        $('#person-position_course').val(data.data.items[0].level.name + ' ' + data.data.items[0].group.name);
                    } else {

                    }
                },
            });
        } else {
            $.ajax({
                url: '/uz/profile/get-teacher-data',
                method: 'GET',
                data: {
                    search: person_id,
                    lang: 'uz-UZ',
                },
                success: function (data) {
                    if (data.success == true && data.data.items[item]) {
                        var first_name = data.data.items[item].first_name;
                        var second_name = data.data.items[item].second_name;
                        var third_name = data.data.items[item].third_name;
                        var staffPosition = data.data.items[item].staffPosition.name;

                        $('#person-person_id').val(data.data.items[item].employee_id_number);

                        $('#user-avatar-photo').attr('src',data.data.items[item].image);
                        $('#hemis-avatar').val(data.data.items[item].image);

                        $('#input-user-firstname:disabled').val(first_name);
                        $('#user-firstname').val(first_name);

                        $('#input-user-lastname:disabled').val(second_name);
                        $('#user-lastname').val(second_name);

                        $('#input-user-middlename:disabled').val(third_name);
                        $('#user-middlename').val(third_name);

                        $('#input-user-staffposition:disabled').val(staffPosition);
                        $('#user-staffposition').val(staffPosition);
                    } else {

                    }
                },
            });
        }
    }
    $('#userSearch').keyup(function () {
        if (this.value.length >= 2) {
            smartSearch(this.value)
        }
    });

    function smartSearch(query) {
        if (query.length > 2) {
            $('#search-result').show();
            smartSearchResult(query);
        } else {
            $('#search-result').hide();
        }
    }
    function smartSearchResult(search) {
        var lang = $('#lang').val();
        var html = '';
        $.ajax({
            url: 'user-search',
            method: "GET",
            type: 'json',
            data: {
                query: search, lang: lang,
            },
            success: function (data) {
                var successTitle = '';
                if (lang == 'ru'){
                    successTitle = 'Информация не найдена';
                } else if (lang == 'en') {
                    successTitle = 'No information found';
                } else if (lang == 'uz') {
                    successTitle = 'Ma\'lumot topilmadi';
                }
                if (data !== null) {
                    for (var i =0; i < data.length; i++){
                        var full_name = data[i].lastname + ' ' + data[i].firstname + ' ' + data[i].middlename;
                        html += '<a href="/' + lang + '/profile/' + data[i].id + '"><div class="search-item-user">' + full_name +
                            '</div></a>';
                    }
                    $('#search-result').html(html);
                } else {
                    html += '<a><div class="search-item-user">' + successTitle + '</div></a>';
                    $('#search-result').html(html);
                }

                console.log(html);
            }
        })
    }

});
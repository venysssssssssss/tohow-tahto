function datatables() {
    return {
        headings: [
            {
                'key': 'codSkill',
                'value': 'Cód. SKILL'
            },
            {
                'key': 'vdn',
                'value': 'VDN'
            },
            {
                'key': 'actionType',
                'value': 'Tipo Ação'
            },
            {
                'key': 'name',
                'value': 'Nome'
            },
            {
                'key': 'cellType',
                'value': 'Tipo Célula'
            },
            {
                'key': 'site',
                'value': 'Site'
            },
            {
                'key': 'serviceHours',
                'value': 'Horário de atendimento'
            },
            {
                'key': 'skillTelevendas',
                'value': 'SKILL TELEVENDAS (CNG 0303)'
            },
            {
                'key': 'audioCliente',
                'value': 'AUDIO CLIENTE (CALL BACK)'
            },
            {
                'key': 'arvoreQA',
                'value': 'Árvore QA'
            },
            {
                'key': 'botaoDesligarChamadas',
                'value': 'Botão para Desligar Chamadas?'
            },
            {
                'key': 'restricaoDesligarChamadas',
                'value': 'Restrição para Desligar Chamadas'
            },
            {
                'key': 'botaoConferencia',
                'value': 'Botão Conferência'
            },
            {
                'key': 'botaoEspera',
                'value': 'Botão Espera'
            },
            {
                'key': 'callBackPopUpAutomatica',
                'value': 'Call back Pop up Automática'
            },
            {
                'key': 'callBackManualRestrito',
                'value': 'Call back Manual Restrito'
            },
            {
                'key': 'incluirSkillPosRouting',
                'value': 'Incluir Skill no PÓS ROUTING?'
            },
            {
                'key': 'acw',
                'value': 'ACW'
            },
            {
                'key': 'botaoMakeCall',
                'value': 'Botão Make Call'
            },
            {
                'key': 'funcionalidadesToolbar',
                'value': 'Funcionalidades do Toolbar'
            },
            {
                'key': 'informarProcessoRPA',
                'value': 'Informar qual será o processo (RPA)?'
            },
            {
                'key': 'skillPossuiURL',
                'value': 'SKILL:possuíra URL será aberta por "fora" da toolbar?'
            },
            {
                'key': 'url',
                'value': 'URL'
            }
        ],
        
        users: [{
            "userId": 1,
            "firstName": "Cort",
            "lastName": "Tosh",
            "emailAddress": "ctosh0@github.com",
            "gender": "Male",
            "phoneNumber": "327-626-5542",
            "serviceHours": "08:00 - 18:00"
        }, {
            "userId": 2,
            "firstName": "Brianne",
            "lastName": "Dzeniskevich",
            "emailAddress": "bdzeniskevich1@hostgator.com",
            "gender": "Female",
            "phoneNumber": "144-190-8956"
        }, {
            "userId": 3,
            "firstName": "Isadore",
            "lastName": "Botler",
            "emailAddress": "ibotler2@gmpg.org",
            "gender": "Male",
            "phoneNumber": "350-937-0792"
        }, {
            "userId": 4,
            "firstName": "Janaya",
            "lastName": "Klosges",
            "emailAddress": "jklosges3@amazon.de",
            "gender": "Female",
            "phoneNumber": "502-438-7799"
        }, {
            "userId": 5,
            "firstName": "Freddi",
            "lastName": "Di Claudio",
            "emailAddress": "fdiclaudio4@phoca.cz",
            "gender": "Female",
            "phoneNumber": "265-448-9627"
        }, {
            "userId": 6,
            "firstName": "Oliy",
            "lastName": "Mairs",
            "emailAddress": "omairs5@fda.gov",
            "gender": "Female",
            "phoneNumber": "221-516-2295"
        }, {
            "userId": 7,
            "firstName": "Tabb",
            "lastName": "Wiseman",
            "emailAddress": "twiseman6@friendfeed.com",
            "gender": "Male",
            "phoneNumber": "171-817-5020"
        }, {
            "userId": 8,
            "firstName": "Joela",
            "lastName": "Betteriss",
            "emailAddress": "jbetteriss7@msu.edu",
            "gender": "Female",
            "phoneNumber": "481-100-9345"
        }, {
            "userId": 9,
            "firstName": "Alistair",
            "lastName": "Vasyagin",
            "emailAddress": "avasyagin8@gnu.org",
            "gender": "Male",
            "phoneNumber": "520-669-8364"
        }, {
            "userId": 10,
            "firstName": "Nealon",
            "lastName": "Ratray",
            "emailAddress": "nratray9@typepad.com",
            "gender": "Male",
            "phoneNumber": "993-654-9793"
        }, {
            "userId": 11,
            "firstName": "Annissa",
            "lastName": "Kissick",
            "emailAddress": "akissicka@deliciousdays.com",
            "gender": "Female",
            "phoneNumber": "283-425-2705"
        }, {
            "userId": 12,
            "firstName": "Nissie",
            "lastName": "Sidnell",
            "emailAddress": "nsidnellb@freewebs.com",
            "gender": "Female",
            "phoneNumber": "754-391-3116"
        }, {
            "userId": 13,
            "firstName": "Madalena",
            "lastName": "Fouch",
            "emailAddress": "mfouchc@mozilla.org",
            "gender": "Female",
            "phoneNumber": "584-300-9004"
        }, {
            "userId": 14,
            "firstName": "Rozina",
            "lastName": "Atkins",
            "emailAddress": "ratkinsd@japanpost.jp",
            "gender": "Female",
            "phoneNumber": "792-856-0845"
        }, {
            "userId": 15,
            "firstName": "Lorelle",
            "lastName": "Sandcroft",
            "emailAddress": "lsandcrofte@google.nl",
            "gender": "Female",
            "phoneNumber": "882-911-7241"
        }],
        selectedRows: [],

        open: false,

        // Adicionar esta função no objeto retornado pela função datatables()
        updateUser(user, key, value) {
            // Encontrar o índice do usuário no array users
            const index = this.users.findIndex(u => u.userId === user.userId);
            // Atualizar o valor correspondente no usuário
            this.users[index][key] = value;
        },

        
        toggleColumn(key) {
            // Note: All td must have the same class name as the headings key! 
            let columns = document.querySelectorAll('.' + key);

            if (this.$refs[key].classList.contains('hidden') && this.$refs[key].classList.contains(key)) {
                columns.forEach(column => {
                    column.classList.remove('hidden');
                });
            } else {
                columns.forEach(column => {
                    column.classList.add('hidden');
                });
            }
        },

        getRowDetail($event, id) {
            let rows = this.selectedRows;

            if (rows.includes(id)) {
                let index = rows.indexOf(id);
                rows.splice(index, 1);
            } else {
                rows.push(id);
            }
        },

        selectAllCheckbox($event) {
            let columns = document.querySelectorAll('.rowCheckbox');

            this.selectedRows = [];

            if ($event.target.checked == true) {
                columns.forEach(column => {
                    column.checked = true
                    this.selectedRows.push(parseInt(column.name))
                });
            } else {
                columns.forEach(column => {
                    column.checked = false
                });
                this.selectedRows = [];
            }
        }
    }
}

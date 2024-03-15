//material contact form animation
$('.contact-form').find('.form-control').each(function() {
    var targetItem = $(this).parent();
    if ($(this).val()) {
      $(targetItem).find('label').css({
        'top': '10px',
        'fontSize': '14px'
      });
    }
  })
  $('.contact-form').find('.form-control').focus(function() {
    $(this).parent('.input-block').addClass('focus');
    $(this).parent().find('label').animate({
      'top': '10px',
      'fontSize': '14px'
    }, 300);
  })
  $('.contact-form').find('.form-control').blur(function() {
    if ($(this).val().length == 0) {
      $(this).parent('.input-block').removeClass('focus');
      $(this).parent().find('label').animate({
        'top': '25px',
        'fontSize': '18px'
      }, 300);
    }
  })

  function formatDate(input) {
    // Remove qualquer caractere não numérico
    var inputValue = input.value.replace(/\D/g, '');
    
    // Adiciona a barra após o segundo dígito para o dia e o mês
    if (inputValue.length > 2 && inputValue.charAt(2) !== '/') {
      inputValue = inputValue.slice(0, 2) + '/' + inputValue.slice(2);
    }
    
    // Adiciona a barra após o quinto dígito para o ano
    if (inputValue.length > 5 && inputValue.charAt(5) !== '/') {
      inputValue = inputValue.slice(0, 5) + '/' + inputValue.slice(5);
    }
    
    // Limita a entrada a 10 caracteres
    input.value = inputValue.slice(0, 10);
  }

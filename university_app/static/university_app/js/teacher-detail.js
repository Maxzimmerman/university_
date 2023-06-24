$(function () {
  $(".close-button").hide(10)
  $(".detail-card").hover(
    function () {
        $(".detail-card").hide(1000)
        $(".form-button").show(1000)
    },
  )
  $(".close-button").on("click", function () {
      $(".detail-card").show(1000)
      $(".form-button").hide(1000)
      $("#modals-here").slideUp(1000)
      $(".close-button").hide(10)
  })
  $(".form-button").on("click", function () {
      $(".close-button").show(1000)
      $("#modals-here").slideDown(1000)
  })
})

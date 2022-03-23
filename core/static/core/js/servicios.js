var removeActiveClass = function () {
    $(".agricultura").removeClass("activo");
    $(".acuicultura").removeClass("activo");
    $(".aguas").removeClass("activo");
    $(".algas").removeClass("activo");
    $(".pool").removeClass("activo");
    $(".laundry").removeClass("activo");
    $(".golf").removeClass("activo");
    $(".garden").removeClass("activo");
    $(".chemistry").removeClass("activo");
    $(".oil").removeClass("activo");
    $(".miner").removeClass("activo");
  };

  $(function () {
    $(".agricultura").click(function () {
      removeActiveClass();
      $(".agricultura").addClass("activo");
      document.getElementById("services").className = "agri";
    });

    $(".acuicultura").click(function () {
      removeActiveClass();
      $(".acuicultura").addClass("activo");
      document.getElementById("services").className = "acui";
    });

    $(".aguas").click(function () {
      removeActiveClass();
      $(".aguas").addClass("activo");
      document.getElementById("services").className = "water";
    });

    $(".algas").click(function () {
      removeActiveClass();
      $(".algas").addClass("activo");
      document.getElementById("services").className = "algae";
    });

    $(".pool").click(function () {
      removeActiveClass();
      $(".pool").addClass("activo");
      document.getElementById("services").className = "piscina";
    });

    $(".laundry").click(function () {
      removeActiveClass();
      $(".laundry").addClass("activo");
      document.getElementById("services").className = "washer";
    });

    $(".golf").click(function () {
      removeActiveClass();
      $(".golf").addClass("activo");
      document.getElementById("services").className = "hoyo";
    });

    $(".garden").click(function () {
      removeActiveClass();
      $(".garden").addClass("activo");
      document.getElementById("services").className = "jardin";
    });

    $(".chemistry").click(function () {
      removeActiveClass();
      $(".chemistry").addClass("activo");
      document.getElementById("services").className = "quimica";
    });

    $(".oil").click(function () {
      removeActiveClass();
      $(".oil").addClass("activo");
      document.getElementById("services").className = "gas";
    });

    $(".miner").click(function () {
      removeActiveClass();
      $(".miner").addClass("activo");
      document.getElementById("services").className = "mineria";
    });
  });

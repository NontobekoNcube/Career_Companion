document.addEventListener("DOMContentLoaded", async function () {
  try {
    const response = await fetch("/frontend/components/navbar.html");
    const navbarHTML = await response.text();
    document.getElementById("nav-container").innerHTML = navbarHTML;
  } catch (error) {
    console.error("Error loading navbar:", error);
  }
});

const next = () => {
  const prevDiv = document.querySelector("#prev");
  const nextDiv = document.querySelector("#next");
  nextDiv.removeAttribute("hidden")
  prevDiv.setAttribute("hidden", true)

  nextDiv.classList.add('next')

  const submitBtn = document.querySelector("#submit");
  submitBtn.removeAttribute("hidden");

  const btnNext = document.querySelector("#btnNext");
  btnNext.setAttribute("hidden", true);
}

const prev = () => {
  const nextDiv = document.querySelector("#next");
  const prevDiv = document.querySelector("#prev");
  prevDiv.removeAttribute("hidden")
  nextDiv.setAttribute("hidden", true)

  nextDiv.classList.remove('next')

  const submitBtn = document.querySelector("#submit");
  submitBtn.setAttribute("hidden", true);

  const btnNext = document.querySelector("#btnNext");
  btnNext.removeAttribute("hidden");
}
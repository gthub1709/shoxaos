const contactBtns = document.querySelectorAll(".contact-btn");
const modal = document.querySelector("#modal");
const modalContent = document.querySelector(".modal-container");
const modalSubmitBtn = document.querySelector("#modal-submit");
const modalForm = document.querySelector("#modal-form");
const successBlock = document.querySelector(".success-submit");
const closeModalBtn = document.querySelector(".close-modal__btn");
const closeSuccessBtn = document.querySelector(".close-success");
const superSuccessBtn = document.querySelector(".success-submit__btn");
const cookies = document.querySelector(".cookies");
const acceptBtn = document.querySelector("#accept-btn");
const declineBtn = document.querySelector("#decline-btn");
const closeCookies = document.querySelector("#cookies-close");
const burgerBtn = document.querySelector(".burger-btn");
const burgerMenu = document.querySelector(".burger-menu");
const burgerMenuCloseBtn = document.querySelector(".burger-menu__close");
const phoneInput = document.querySelector("#phone");

burgerBtn.addEventListener("click", () => {
    burgerMenu.classList.add("active");
})

burgerMenuCloseBtn.addEventListener("click", () => {
    burgerMenuCloseBtn.classList.add("active");
    burgerMenu.classList.remove("active");
})

const fields = [
    { id: "name", errorId: "name-error" },
    { id: "email", errorId: "email-error" },
    { id: "phone", errorId: "phone-error" },
];

const showError = (field, error, errorMain) => {
    error.style.display = "block";
    errorMain.style.display = "block";
};

const hideError = (error, errorMain) => {
    error.style.display = "none";
    errorMain.style.display = "none";
};

const initializeCookiesConsent = () => {
    cookies.classList.add("active");

    const handleCookieConsent = () => {
        cookies.classList.remove("active");
    };

    acceptBtn.addEventListener("click", handleCookieConsent);
    declineBtn.addEventListener("click", handleCookieConsent);
    closeCookies.addEventListener("click", handleCookieConsent);
};

const initializeModalFormValidation = () => {
    modalSubmitBtn.disabled = true;

    const validateField = (field, error, errorMain) => {
        field.addEventListener("blur", () => {
            if (!field.value.trim()) {
                showError(field, error, errorMain);
            } else {
                hideError(error, errorMain);
            }
            validateForm();
        });
    };

    const validateForm = () => {
        const isValid = fields.every(({ id }) => {
            const field = document.querySelector(`#${id}`);
            return field.value.trim();
        });

        modalSubmitBtn.disabled = !isValid;
    };

    fields.forEach(({ id, errorId }) => {
        const field = document.querySelector(`#${id}`);
        const error = document.querySelector(`#${errorId}`);
        const errorMain = document.querySelector("#error-main");
        validateField(field, error, errorMain);
    });
};

const openModal = () => {
    modal.classList.add("active");
};

const closeModal = () => {
    modal.classList.remove("active");
};

const handleFormSubmit = (e) => {
    e.preventDefault();

    fields.forEach(({ id }) => {
        const field = document.querySelector(`#${id}`);
        field.value = "";
    });

    modal.classList.remove("active");
    successBlock.classList.add("active");
};

const closeSuccessBlock = () => {
    successBlock.classList.remove("active");
};

const initializeEventListeners = () => {
    contactBtns.forEach((btn) => btn.addEventListener("click", openModal));

    modal.addEventListener("click", closeModal);
    modalContent.addEventListener("click", (e) => e.stopPropagation());

    closeModalBtn.addEventListener("click", closeModal);

    closeSuccessBtn.addEventListener("click", closeSuccessBlock);
    superSuccessBtn.addEventListener("click", closeSuccessBlock);

    modalForm.addEventListener("submit", handleFormSubmit);
};


window.onload = () => {
    initializeCookiesConsent();
    initializeModalFormValidation();
    initializeEventListeners();
};

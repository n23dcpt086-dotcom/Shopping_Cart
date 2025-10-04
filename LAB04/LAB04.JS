document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Ngăn chặn việc form được submit theo cách truyền thống
    event.preventDefault(); 
    
    // Thực hiện kiểm tra dữ liệu
    if (validateForm()) {
       
        console.log('Đăng nhập thành công! (Chuyển hướng người dùng...)');
        alert('Đăng nhập thành công!');
       
    } else {
        console.log('Lỗi đăng nhập: Dữ liệu nhập không hợp lệ.');
    }
});

function validateForm() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    let isValid = true;

    // Reset lỗi
    usernameError.textContent = '';
    passwordError.textContent = '';
    usernameInput.classList.remove('input-error');
    passwordInput.classList.remove('input-error');

    // 1. Kiểm tra Username (Tên người dùng)
    if (usernameInput.value.trim() === '') {
        usernameError.textContent = 'Tên người dùng không được để trống.';
        usernameInput.classList.add('input-error');
        isValid = false;
    } else if (usernameInput.value.trim().length < 5) {
        usernameError.textContent = 'Tên người dùng phải có ít nhất 5 ký tự.';
        usernameInput.classList.add('input-error');
        isValid = false;
    }

    // 2. Kiểm tra Password (Mật khẩu)
    if (passwordInput.value.trim() === '') {
        passwordError.textContent = 'Mật khẩu không được để trống.';
        passwordInput.classList.add('input-error');
        isValid = false;
    } else if (passwordInput.value.trim().length < 8) {
        passwordError.textContent = 'Mật khẩu phải có ít nhất 8 ký tự.';
        passwordInput.classList.add('input-error');
        isValid = false;
    }
    

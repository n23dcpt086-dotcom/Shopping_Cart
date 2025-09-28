document.getElementById('loginForm').addEventListener('submit', function(event) {
    
    event.preventDefault();

    
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('rememberMe').checked;
    const messageElement = document.getElementById('message');

    // Xóa thông báo cũ
    messageElement.style.display = 'none';
    messageElement.classList.remove('success', 'error');
    messageElement.textContent = '';


    // 1. Kiểm tra không được để trống
    if (username === '' || password === '') {
        displayMessage('Vui lòng nhập đầy đủ Tên người dùng và Mật khẩu.', 'error');
        return;
    }

    // 2. Kiểm tra độ dài Tên người dùng (tối thiểu 4 ký tự)
    if (username.length < 4) {
        displayMessage('Tên người dùng phải có ít nhất 4 ký tự.', 'error');
        return;
    }

    // 3. Kiểm tra độ dài Mật khẩu (tối thiểu 6 ký tự)
    if (password.length < 6) {
        displayMessage('Mật khẩu phải có ít nhất 6 ký tự.', 'error');
        return;
    }

    // 4. Kiểm tra Mật khẩu có chứa số và chữ cái
    const hasLetter = /[a-zA-Z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    if (!hasLetter || !hasNumber) {
        displayMessage('Mật khẩu phải chứa cả chữ cái và số.', 'error');
        return;
    }

    // --- XỬ LÝ ĐĂNG NHẬP THÀNH CÔNG (Mô phỏng) ---

    // đăng nhập thành công
    if (username === 'admin' && password === 'admin123') {
        let successMsg = 'Đăng nhập thành công! Chào mừng ' + username + '.';
        if (rememberMe) {
            successMsg += ' (Tài khoản đã được ghi nhớ.)';
        }
        displayMessage(successMsg, 'success');

        // setTimeout(() => {
        //     window.location.href = 'dashboard.html';
        // }, 2000);

    } else {
        displayMessage('Tên người dùng hoặc Mật khẩu không đúng.', 'error');
    }
});

// Hàm hiển thị thông báo
function displayMessage(text, type) {
    const messageElement = document.getElementById('message');
    messageElement.textContent = text;
    messageElement.classList.add(type); 
    messageElement.style.display = 'block';
}
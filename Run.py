import re

class TestRunBuilder:
    pattern = "[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"

    def __init__(self, username, user_email, user_password):
        if len(username) < 4 or len(username) > 25:
            raise Exception("username  can't be with length less 4 "
                            "characters and more 25 characters")
        self.username = username;

        number_re = re.compile(self.pattern);
        if not number_re.findall(user_email):
            raise Exception("e-mail should contain '@',  '.' characters ")
        self.user_email = user_email;

        if len(user_password) < 8 or len(user_password) > 25:
            raise Exception("user password  can't be with length less 8 "
                            "characters and more 25 characters")
        self.user_password = user_password;

    def test_login_suit(self):
        print("login_suit:");
        print("User clicks on Sign In link ")
        print("User enters email: " + self.user_email);
        print("User enters password: " + self.user_password);
        print("User clicks on button [Sign in]")
        print("User logs in their account ")

    def test_registration_suit(self):
        print("registration_suit:");
        print("User clicks on Sign Up link ")
        print("User enters username: " + self.username);
        print("User enters password: " + self.user_password);
        print("User enters e-mail: " + self.user_email);
        print("User clicks on button [Sign in]")
        print("User creates and is redirected to their account ")

    def test_article_suit(self):
        print("article_suit:");
        print("User clicks on New Post ")
        print("User enters Article Title ")
        print("User enters 'What's this article about?' field ")
        print("User enters 'Tag' field ")
        print("User clicks on button [Publish Article]")
        print("User redirects to their article page")

    def test_run_smoke(self):
        print("test_run_smoke:");
        self.test_login_suit();
        self.test_registration_suit();
        print("\n");

    def test_run_sanity(self):
        print("test_run_sanity for login:");
        self.test_login_suit();
        print("\n");

    def test_run_regression(self):
        print("test_run_regression")
        self.test_login_suit();
        self.test_article_suit();
        self.test_registration_suit();
        print("\n");

test_run_smoke = TestRunBuilder("dima", "dimalitvin192.0@gmail.com","amid1516")
test_run_smoke.test_run_smoke();

test_run_sanity = TestRunBuilder("ruslan", "ruslan98@gmail.com", "rus25997")
test_run_sanity.test_run_sanity();

test_run_regression = TestRunBuilder("tanya", "tet@gmail.com", "ayat5620")
test_run_regression.test_run_regression();


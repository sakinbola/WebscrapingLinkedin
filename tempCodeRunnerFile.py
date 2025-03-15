while driver.window_handles:
    driver.get("https://www.linkedin.com/jobs/")

    assert "LinkedIn" in driver.title
    # do you ahve right webpage 

    choice = input("Press Y to continue: ").strip().lower()
    if choice == "y":
        print("You pressed Y website is correct")
    else:
        print("error")

    driver.quit()
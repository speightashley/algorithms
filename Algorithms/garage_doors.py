def controller(events):
    current_state = "closed"
    action = 0
    collection_of_actions = []

    for event in events:
        if action == 0:
            current_state = "closed"

        elif action == 5:
            current_state = "open"

        if current_state == "closed":
            if event == "P":
                action += 1
                current_state = "opening"
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                collection_of_actions.append(str(action))
                continue

        if current_state == "opening":
            if event == "P":
                current_state = "blocked_opening"
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                action += 1
                collection_of_actions.append(str(action))
                continue

            elif event == "O":
                current_state = "closing"
                action -= 1
                collection_of_actions.append(str(action))
                continue

        if current_state == "blocked_opening":
            if event == "P":
                current_state = "opening"
                action += 1
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                collection_of_actions.append(str(action))
                continue

            elif event == "O":
                current_state = "closing"
                action -= 1
                collection_of_actions.append(str(action))
                continue

        if current_state == "open":
            if event == "P":
                current_state = "closing"
                action -= 1
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                collection_of_actions.append(str(action))
                continue

            elif event == "O":
                current_state = "closing"
                action -= 1
                collection_of_actions.append(str(action))
                continue

        if current_state == "closing":
            if event == "P":
                current_state = "blocked_closing"
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                action -= 1
                collection_of_actions.append(str(action))
                continue

            elif event == "O":
                current_state = "opening"
                action += 1
                collection_of_actions.append(str(action))
                continue

        if current_state == "blocked_closing":
            if event == "P":
                current_state = "closing"
                action += 1
                collection_of_actions.append(str(action))
                continue

            elif event == ".":
                collection_of_actions.append(str(action))
                continue

            elif event == "O":
                current_state = "opening"
                action += 1
                collection_of_actions.append(str(action))
                continue

    answer = "".join(collection_of_actions)

    return answer


print(controller('..........'))  # '0000000000'
print(controller('P....')) # '12345')

print(controller('P.P..')) #'12222')

print(controller('..P...O...')) # '0012343210')
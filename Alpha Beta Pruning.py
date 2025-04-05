def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node['children']:
        return node['value']
    
    if maximizing_player:
        max_eval = float('-inf') 
        for child in node['children']:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node['children']:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


game_tree = {
    'value': None,
    'children': [
        {
            'value': None,
            'children': [
                {'value': 3, 'children': []},
                {'value': 12, 'children': []},
                {'value': 8, 'children': []}
            ]
        },
        {
            'value': None,
            'children': [
                {'value': 2, 'children': []},
                {'value': 5, 'children': []},
                {'value': 1, 'children': []}
            ]
        }
    ]
}

optimal_value = alpha_beta_pruning(game_tree, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
print(f"The optimal value is: {optimal_value}")

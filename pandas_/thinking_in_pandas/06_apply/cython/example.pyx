from scipy.stats import percentileofscore as pct_of_score


# Without cython
# def get_percentile_of_score_base(df, score):
#     res_df = pd.DataFrame({})
#     for col in df.columns:
#         score = pd.DataFrame([df[col]] * 5, index=df.columns).T
#         left = df[df < score].count(axis=1)
#         right = df[df <= score].count(axis=1)
#         right_is_greater = (right > left).astype(int)
#         res_df[f'res_{col}'] = (
#             (left + right + right_is_greater) * 50. / len(df.columns))
#    return res_df


# Better
def get_percentile_of_score(values):
    percentiles = [0] * len(values[0])
    n_rows = len(values)
    for r in range(n_rows):
        r_vals = values[r]
        for c, c_val in enumerate(r_vals):
            percentiles[c] = pct_of_score(r_vals, c_val)
        values[r] = percentiles
    return values

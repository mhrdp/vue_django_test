<template>
	<div class="card mb-4">
		<div class="card-body">
			<h5><strong>{{obj.userdata.username}}</strong></h5>
			<p class="text-muted fs-7 fw-light">
				<span>{{obj.date_posted.slice(0, 10)}}</span>
				<span>{{obj.date_posted.slice(11, 16)}}</span>
			</p>
			<p>{{obj.post.slice(0, 300)}} <span>....</span></p>
			<router-link v-bind:to="obj.get_absolute_url">
				<button class="btn btn-sm btn-secondary">
					Read More
				</button>
			</router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Timeline',
	props: {
		obj: Object
	}
}
</script>
